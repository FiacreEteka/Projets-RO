#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:21:03 2026

@author: fiacre
"""

import numpy as np
import pandas as pd
from geneticalgorithm import geneticalgorithm as ga



df_parcelle = pd.read_csv('../data/parcelles.csv', index_col=0)
df_marches = pd.read_csv('../data/marches.csv', index_col=0)
df_transport = pd.read_csv('../data/couts_transport.csv', index_col=0)
df_temps = pd.read_csv('../data/temps_transport.csv', index_col=0)
df_parametres = pd.read_csv('../data/parametres.csv', index_col=0)


parcelles = list(df_parcelle.index)
marches  = list(df_marches.index)

profit = {}
couts = {}
temps = {}

production = df_parcelle['production'].to_dict()
demande = df_marches['demande_max'].to_dict()
nVars = len(production)*len(marches)

for i in parcelles:
    for j in marches:
        p_j = df_marches.loc[j, 'prix']
        couts[i, j] = df_transport.loc[i, j]
        temps[i, j] = df_temps.loc[i, j]
        profit[i, j] = p_j*(1 - temps[i, j]*0.02) - couts[i, j]

def f(X):
    
    x = {}
    idx = 0
    for i in parcelles:
        for j in marches:
            x[i, j] = X[idx]
            idx += 1
    
    pen = 0  
    
    for i in parcelles:
        total_vendu = sum(x[i, j] for j in marches)
        if total_vendu > production[i]:
            pen += 1e6 * (total_vendu - production[i])
     
    for j in marches:
        total_arrive = sum(x[i, j] * (1 - 0.02 * temps[i, j]) for i in parcelles)
        if total_arrive > demande[j]:
            pen += 1e6 * (total_arrive - demande[j])
     
    quantite_totale = sum(x[i, j] for i in parcelles for j in marches)
    if quantite_totale > 20:       
        pen += 1e6 * (quantite_totale - 20)
        
    obj = sum(profit[i, j] * x[i, j] for i in parcelles for j in marches)
    
    return float(-obj + pen)


varbound = np.array([[0, 8]]*nVars)

model=ga(function=f,\
            dimension=nVars,\
            variable_type='real',\
            variable_boundaries=varbound)
    

model.run()

solutions = model.output_dict

variables_optimales = solutions['variable']

# Reconstruire solution
x_optimal = {}
idx = 0
for i in parcelles:
    for j in marches:
        x_optimal[i, j] = variables_optimales[idx]
        idx += 1

print(x_optimal)


profit_max = -solutions['function']


print(f"Profit Maximal : {profit_max:,.0f} FCFA")
print("Flux de livraison :")
for i in parcelles:
    for j in marches:
        if x_optimal[i, j] > 0.1:
            recu = x_optimal[i, j] * (1 - 0.02 * temps[i, j])
            print(f"  {i} vers {j} : {x_optimal[i,j]:.2f} t expédiées, {recu:.2f} t reçues")





