#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:19:36 2026

@author: fiacre
"""

import pandas as pd

df_parcelle = pd.read_csv('../data/parcelles.csv', index_col=0)
df_marches = pd.read_csv('../data/marches.csv', index_col=0)
df_transport = pd.read_csv('../data/couts_transport.csv', index_col=0)
df_temps = pd.read_csv('../data/temps_transport.csv', index_col=0)
df_parametres = pd.read_csv('../data/parametres.csv', index_col=0)


parcelles = list(df_parcelle.index)
marches  = list(df_marches.index)

profit = {}
x = {}
production = df_parcelle['production'].to_dict()
demande = df_marches['demande_max'].to_dict()

for i in parcelles:
    for j in marches:
        p_j = df_marches.loc[j, 'prix']
        c_ij = df_transport.loc[i, j]
        t_ij = df_temps.loc[i, j]
        x[i, j] = 0
        profit[i, j] = p_j*(1 - t_ij*0.02) - c_ij
        
profit_trie = dict(sorted(profit.items(), key = lambda item: item[1], reverse=True))

cap = capacite_transport = df_parametres.loc['capacite_transport', 'valeur']
prod = production.copy()
dem = demande.copy()

for i, j in  profit_trie.keys():
    facteur_perte = 1 - 0.02 * df_temps.loc[i, j]
    x[i, j] = min(prod[i], dem[j]/facteur_perte, cap)
    
    reçu = x[i, j]*facteur_perte
    cap -= x[i, j]
    prod[i] -= x[i, j]
    dem[j] -= reçu
    
Profit = 0
print("Quantité envoyée des parcelles vers les marchés")

for i in parcelles:
    for j in marches:
        if x[i, j] > 0:
            reçue = x[i, j] * (1 - 0.02 * df_temps.loc[i, j])
            print(f"  {i} vers {j} : {x[i,j]:.2f} t expédiées, {reçue:.2f} t reçues")
            Profit += x[i, j]*profit[i, j]
print(f"rofit total : {Profit:.0f} FCFA")
print(f"Capacité utilisée : {capacite_transport - cap:.1f}/20 t")






