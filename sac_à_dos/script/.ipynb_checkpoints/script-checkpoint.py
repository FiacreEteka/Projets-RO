import pandas as pd
from ortools.sat.python import cp_model

def charger_donnees(chemins_objets, chemin_parametres):
    df_objet = pd.read_csv(chemins_objets, index_col=0)
    df_capacite = pd.read_csv(chemin_parametres, index_col=0)
    objets = list(df_objet.index)
    capacite_max = df_capacite.iloc[0,0]
    poids = df_objet['poids'].to_dict()
    valeur = df_objet['valeur'].to_dict()
    return objets, capacite_max, poids, valeur


def construire_modele(objets, capacite_max, poids, valeur):
    model = cp_model.CpModel()

    # variables de décision
    x = {}
    for objet in objets:
        x[objet] = model.NewBoolVar(f'x_{objet}')
    
    # contraintes 
    model.Add(
        cp_model.LinearExpr.WeightedSum([x[i] for i in objets], [poids[i] for i in objets]) <= capacite_max
    )
    
    # fonction objectif
    model.maximize(
        cp_model.LinearExpr.WeightedSum([x[i] for i in objets], [valeur[i] for i in objets])
    )

    return model, x

def afficher_resultat(model, x, poids, objets):
    solver = cp_model.CpSolver()
    status = solver.solve(model)
    
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Valeur totale: {solver.objective_value}\n")
        for i, var in x.items():
            if solver.value(var) == 1:
                print(f"{i}: sélectionné")
        print(f"Poids total    : {sum(poids[i] for i in objets if solver.value(x[i]) == 1)}")   
        print(f"Statut         : {solver.StatusName()}")
    else:
        print("No solution found.")


if __name__ == '__main__':
    objets, capacite_max, poids, valeur = charger_donnees(
        '../data/objets.csv',
        '../data/parametres.csv'
    )

    model, x = construire_modele(objets, capacite_max, poids, valeur)
    afficher_resultat(model, x, poids, objets)