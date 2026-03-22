# diete.py

import pandas as pd
import pulp as plp
solver = plp.GLPK_CMD(path="/usr/bin/glpsol")  

def charger_donnees(chemin_aliments, chemin_besoins):
    aliment_df = pd.read_csv(chemin_aliments, index_col=0)
    besoin_df = pd.read_csv(chemin_besoins, index_col=0)
    aliments = list(aliment_df.index)
    nutriments = [col for col in aliment_df.columns if col != 'cout']
    aliment_df[nutriments] = aliment_df[nutriments] / 100
    aliment_df['cout'] = aliment_df['cout'] / 100
    besoins = besoin_df['minimum'].to_dict()
    cout = {i : aliment_df.loc[i, 'cout'] for i in aliments}
    return aliments, nutriments, cout, besoins, aliment_df

def construire_modele(aliments, nutriments, cout, besoins, aliment_df, qte_max=300):
    # Modèle
    model = plp.LpProblem("Diète", plp.LpMinimize)

    # Variables
    x  = plp.LpVariable.dicts("x", cout.keys(), lowBound=0, upBound=qte_max, cat='Continuous')

    #  fonction objectif
    model += plp.lpSum([cout[i] * x[i] for i in aliments]), "Coût total"

    # contraintes
    for j in nutriments:
        model += plp.lpSum([aliment_df.loc[i, j]*x[i] for i in aliments]) >= besoins[j] 

    return model, x

def afficher_resultats(model, x):
    # Résolution
    model.solve(solver)
    statut = plp.LpStatus[model.status]
    cout = plp.value(model.objective)
    print(f"Statut de la solution : {statut}")
    print(f"Coût total : {cout:.2f} euros")
    print("Quantités recommandées :")
    for i in x:
        if x[i].varValue > 0:
            print(f" - {i} : {x[i].varValue:.2f} g")
    pass

if __name__ == '__main__':
    aliments, nutriments, cout, besoins, aliment_df = charger_donnees(
        '../data/aliments.csv',
        '../data/besoins.csv'
    )

    model, x = construire_modele(aliments, nutriments, cout, besoins, aliment_df)
    afficher_resultats(model, x)