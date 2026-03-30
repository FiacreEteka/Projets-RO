# Problème du Sac à Dos

## Description
Un randonneur doit choisir quels objets emporter dans son sac à dos 
pour maximiser la valeur totale sans dépasser la capacité maximale de 50 kg.

## Modèle mathématique
- **Variables** : x_i ∈ {0,1} — 1 si l'objet i est sélectionné, 0 sinon
- **Objectif** : Maximiser la valeur totale des objets sélectionnés
- **Contrainte** : Poids total ≤ 50 kg

## Résultats
| Paramètre | Valeur |
|---|---|
| Capacité | 50 kg |
| Valeur optimale | 85 |
| Poids utilisé | 50 kg |
| Objets non sélectionnés | Livre |

## Structure du projet
```
## Structure du projet
```
sac-a-dos/
├── data/
│   ├── objets.csv
│   └── parametres.csv
├── notebooks/
│   └── sac_a_dos.ipynb
├── script/
│   └── script.py
└── README.md
```

## Outils
- Python 3.12
- OR-Tools CP-SAT
- pandas
