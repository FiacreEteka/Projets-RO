# Problème de Tournées de Véhicules (VRP)

## Description
Une entreprise de livraison basée à Paris dispose de 3 véhicules 
(capacité max 100 unités chacun) et doit livrer des colis dans 
10 villes françaises en minimisant la distance totale parcourue.

## Modèle mathématique

### Variables de décision
- **x_ijk ∈ {0,1}** — 1 si le véhicule k va directement de la ville i à la ville j
- **u_i ∈ {1,...,n-1}** — position de la ville i dans la tournée (MTZ)

### Objectif
Minimiser la distance totale : Min Z = Σ_i Σ_j Σ_k d_ij * x_ijk

### Contraintes
- **Degré** : chaque client visité exactement une fois tous véhicules confondus
- **Dépôt** : chaque véhicule part et revient à Paris
- **Flux** : conservation de flux en chaque nœud par véhicule
- **Capacité** : charge de chaque véhicule ≤ 100 unités
- **MTZ** : élimination des sous-tours par véhicule
- **Domaine** : x_ijk ∈ {0,1}, u_i entier

## Résultats

**Distance totale : 3 675 km**

| Véhicule | Tournée | Distance | Charge |
|---|---|---|---|
| V1 | Paris → Toulouse → Bordeaux → Nantes → Rennes → Paris | 1 483 km | 85/100 |
| V2 | Paris → Lille → Paris | 407 km | 25/100 |
| V3 | Paris → Strasbourg → Grenoble → Marseille → Montpellier → Lyon → Paris | 1 784 km | 88/100 |

## Distances calculées
Les distances entre villes sont calculées via la **formule de Haversine** 
à partir des coordonnées GPS réelles des villes françaises.

## Structure du projet
vrp/
├── data/
│ ├── villes.csv
├── notebook/
│ └── VRP.ipynb
├── script/
│ └── script.py
└── README.md

## Outils
- Python 3.12
- PuLP
- GLPK
- pandas