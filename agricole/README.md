# Optimisation d'une Chaîne Logistique Agricole

## Contexte
Une coopérative agricole doit organiser le transport de ses récoltes 
depuis plusieurs parcelles vers différents marchés. L'objectif est de 
maximiser le profit total en tenant compte des coûts de transport, des 
pertes post-récolte liées au temps de trajet, ainsi que des contraintes 
de production, de demande et de capacité de transport.

## Modèle mathématique

### Variables de décision
- **x_ij ≥ 0**  quantité (tonnes) expédiée de la parcelle i vers le marché j

### Profit net par tonne
Le profit unitaire intègre le prix de vente, les pertes liées au temps 
de trajet et le coût de transport :
```
π_ij = p_j × (1 - 0.02 × t_ij) - c_ij
```

### Objectif
Maximiser le profit total : Max Z = Σ_i Σ_j π_ij × x_ij

### Contraintes
- **Production** : la quantité expédiée depuis i ne dépasse pas sa production disponible
- **Demande** : la quantité reçue (après pertes) par j ne dépasse pas sa demande maximale
- **Capacité globale** : la quantité totale transportée ne dépasse pas 20 tonnes
- **Non-négativité** : x_ij ≥ 0

## Méthodes de résolution comparées

Trois approches ont été implémentées et comparées sur la même instance 
(5 parcelles, 3 marchés, capacité 20 t) :

1. **Résolution exacte** (PuLP/GLPK)  référence pour l'évaluation
2. **Heuristique gloutonne**  affectation par ordre décroissant de profit unitaire
3. **Algorithme génétique**  métaheuristique évolutionnaire avec pénalisation des contraintes

## Résultats

| Méthode | Profit (FCFA) | Écart à l'optimal |
|---|---|---|
| Exact (PuLP) | 6 093 445 | (référence) |
| Glouton | 6 093 445 | 0,00 % |
| Algorithme génétique | 6 030 956 | 1,03 % |

### Solution optimale (glouton / exact)

| Flux | Expédié | Reçu |
|---|---|---|
| P2 → M1 | 4.80 t | 4.61 t |
| P2 → M2 | 1.20 t | 1.18 t |
| P3 → M3 | 6.00 t | 5.76 t |
| P5 → M1 | 5.62 t | 5.39 t |
| P5 → M3 | 2.38 t | 2.24 t |

### Analyse

La structure particulière de ce problème de transport permet à 
l'heuristique gloutonne d'atteindre l'optimum exact. L'algorithme 
génétique, ne disposant d'aucune connaissance structurelle du problème 
et travaillant sur des variables continues non contraintes strictement 
(gestion par pénalités), s'en approche à moins de 1,1 % près — au prix 
d'une solution légèrement plus dispersée (petits flux résiduels).

Parcelles P1 et P4, moins compétitives en profit unitaire, ne sont pas 
utilisées par le glouton mais contribuent marginalement dans la 
solution de l'algorithme génétique.

## Structure du projet
```
agricole/
├── data/
│   ├── parcelles.csv
│   ├── marches.csv
│   ├── couts_transport.csv
│   ├── temps_transport.csv
│   └── parametres.csv
├── notebooks/
│   └── agricole.ipynb
├── script/
│   ├── glouton.py
│   └── algo_genetique.py
└── README.md
```

## Outils
- Python 3.12
- PuLP
- GLPK
- geneticalgorithm (algorithme génétique)
- pandas, NumPy
