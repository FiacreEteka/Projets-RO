import pandas as pd
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

def charger_donnees(chemin_cout, chemin_depots, chemin_distances, chemin_parametres, chemin_zones):
    df_depots = pd.read_csv(chemin_depots, index_col=0)
    df_zones = pd.read_csv(chemin_zones, index_col=0)
    df_cout_transports = pd.read_csv(chemin_cout, index_col=0)
    df_parametres = pd.read_csv(chemin_parametres, index_col=0)
    df_distances = pd.read_csv(chemin_distances, index_col=0)

    # Paramètres
    depots = list(df_depots.index)
    zones = list(df_zones.index)
    cout_fixe = df_depots['cout_fixe'].to_dict()
    capacite = df_depots['capacite'].to_dict()
    demandes = df_zones['demande'].to_dict()
    nb_depot_max = df_parametres.loc['nb_depots_max', 'valeur']
    budget_max = df_parametres.loc['budget_max', 'valeur']
    
    cout_transport = {}
    distances = {}
    for i in depots:
        for j in zones:
            cout_transport[i, j] = df_cout_transports.loc[i,j]
            distances[i, j] = df_distances.loc[i,j]

    return depots, zones, cout_fixe, capacite, demandes, nb_depot_max, budget_max, cout_transport, distances


def construire_model(depots, zones, cout_fixe, capacite, demandes, nb_depot_max, budget_max, cout_transport, distances):
    # Modèle
    model = pyo.ConcreteModel()
    
    # Variables de décision
    model.x = pyo.Var(depots, zones, bounds=(0, None), within = Reals)
    model.y = pyo.Var(depots, within = Binary)
    
    x = model.x
    y = model.y
    
    # Fonction onjectif
    model.obj = pyo.Objective(expr = sum(cout_transport[i, j]*x[i, j] for i in depots for j in zones) + sum(y[i]*cout_fixe[i] for i in depots), sense = pyo.minimize)
    
    # Contraintes
    model.c1 = pyo.ConstraintList()
    for j in zones:
        model.c1.add(expr = sum(x[i, j] for i in depots) == demandes[j])
    
    model.c2 = pyo.ConstraintList()
    for i in depots:
        model.c2.add(expr = sum(x[i, j] for j in zones) <= capacite[i]*y[i])
    
    model.c3 = pyo.Constraint(expr = sum(y[i] for i in depots) <= nb_depot_max)
    
    model.c4 = pyo.Constraint(
        expr=sum(cout_fixe[i]*y[i] for i in depots) + 
             sum(cout_transport[i,j]*x[i,j] for i in depots for j in zones) 
             <= budget_max
    )

    return model, x, y

def  afficher_resultat(model, x, y, depots, zones, capacite):
    # Résolution
    opt = SolverFactory('glpk')
    opt.solve(model)
    
    print(f"Coût total : {pyo.value(model.obj):,.0f} FCFA\n")
    
    depots_ouverts = [i for i in depots if pyo.value(y[i]) == 1]
    print(f"Dépôts ouverts ({len(depots_ouverts)}) : {', '.join(depots_ouverts)}\n")
    
    for i in depots_ouverts:
        charge = sum(pyo.value(x[i, j]) for j in zones if pyo.value(x[i, j]) > 0)
        print(f"Dépôt {i} — Charge : {charge:.0f}/{capacite[i]} ")
        for j in zones:
            if pyo.value(x[i, j]) > 0:
                print(f"{j} : {pyo.value(x[i, j]):.0f} ")
        print()

if __name__ == '__main__':
    depots, zones, cout_fixe, capacite, demandes, nb_depot_max, budget_max, cout_transport, distances = charger_donnees("../data/couts_transport.csv",
                                                                                                                        "../data/depots.csv", "../data/distances.csv",
                                                                                                                        "../data/parametres.csv", "../data/zones.csv") 
    
    model, x, y = construire_model(depots, zones, cout_fixe, capacite, demandes, nb_depot_max, budget_max, cout_transport, distances)
    
    afficher_resultat(model, x, y, depots, zones, capacite)
