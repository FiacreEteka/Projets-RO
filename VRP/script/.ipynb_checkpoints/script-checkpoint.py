import pandas as pd
import pulp as plp
from math import radians, sin, cos, sqrt, atan2

nb_vehicules = 3
capacite_max = 100

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2-lat1)
    dlon = radians(lon2-lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return 2*R*atan2(sqrt(a), sqrt(1-a))

def charger_donnees(chemins_objets):
    df = pd.read_csv(chemins_objets, index_col=0)
    demande = df['demande'].to_dict()
    villes = list(df.index)
    depot = villes[0]
    clients = [v for v in df.index if v != depot]
    nb_villes = len(villes)
    distances = {}
    for i in villes:
        for j in villes:
            if i != j:
                distances[i, j] = haversine(df.loc[i, 'latitude'], df.loc[i, 'longitude'], 
                                            df.loc[j, 'latitude'], df.loc[j, 'longitude'])

    return depot, clients, demande, distances, villes, nb_villes


def construire_model(depot, clients, demande, distances, villes, nb_villes):
    model = plp.LpProblem("VRP", plp.LpMinimize)

    # variables de décision
    x = plp.LpVariable.dicts('x', [(i, j, k) for i in villes for j in villes for k in range(1, nb_vehicules+1)], cat = "Binary")
    u = plp.LpVariable.dicts('u', clients, lowBound = 1,upBound = nb_villes - 1, cat='Integers')

    # Fonction objectif
    model += plp.lpSum(distances[i, j]*x[i, j, k] for i in villes for j in villes for k in range(1, nb_vehicules+1) if i!=j)

    # Contraintes
    for j in clients:
        model += plp.lpSum(x[i, j, k] for i in villes for k in range(1, nb_vehicules+1) if i!= j) == 1 

    for i in clients:
        model += plp.lpSum(x[i, j, k] for j in villes for k in range(1, nb_vehicules+1) if i!= j) == 1 

    for k in range(1, nb_vehicules+1):
        model += plp.lpSum(x[i, depot, k] for i in clients) == 1  
        model += plp.lpSum(x[depot, j, k] for j in clients) == 1  
        model += plp.lpSum(demande[i]*x[i, j, k] for i in clients for j in villes if i!=j) <= capacite_max  
        for h in clients:
            model += (plp.lpSum(x[i, h, k] for i in villes if i != h) == 
                    plp.lpSum(x[h, j, k] for j in villes if j != h))

    for i in clients:
        for j in clients:
            for k in range(1, nb_vehicules+1):
                if i != j:
                    model += u[i] - u[j] + nb_villes*x[i, j, k] <= nb_villes - 1

    return model, x

def afficher_resultat(model, x, villes, depot, demande, distances):
    solver = plp.GLPK_CMD()
    model.solve(solver)

    # Résultats
    print(f"Statut : {plp.LpStatus[model.status]}")
    print(f"Distance totale : {plp.value(model.objective):.0f} km\n")

    # Reconstruire les tournées par véhicule
    for k in range(1, 4):
        tournee = [depot]
        ville_actuelle = depot
        distance_k = 0

        while True:
            next_ville = None
            for j in villes:
                if ville_actuelle != j and plp.value(x[ville_actuelle, j, k]) == 1:
                    next_ville = j
                    break
            if next_ville is None:
                break
            distance_k += distances[ville_actuelle, next_ville]
            tournee.append(next_ville)
            ville_actuelle = next_ville
            if next_ville == depot:
                break

        if len(tournee) > 2:
            print(f"Véhicule {k} — Distance : {distance_k:.0f} km")
            print(f"  {' → '.join(tournee)}")
            charge = sum(demande[v] for v in tournee if v != depot)
            print(f"  Charge : {charge}/{capacite_max} unités\n")

if __name__ == '__main__':
    depot, clients, demande, distances, villes, nb_villes = charger_donnees(
        '../data/villes.csv',
    )

    model, x = construire_model(depot, clients, demande, distances, villes, nb_villes)
    afficher_resultat(model, x, villes, depot, demande, distances)