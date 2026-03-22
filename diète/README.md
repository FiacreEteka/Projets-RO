# Problème de Diète

## Description
Modélisation et résolution d'un problème de diète par programmation linéaire.
L'objectif est de composer un menu journalier au coût minimum tout en 
respectant les besoins nutritionnels d'un patient.

## Modèle mathématique
- **Variables** : x_i = quantité de l'aliment i consommée (en grammes)
- **Objectif** : Minimiser le coût total du menu
- **Contraintes** :
  - Apport minimum en calories, protéines, glucides et lipides
  - Quantité par aliment entre 0g et 300g

## Résultats
Menu optimal trouvé pour 2.19€/jour :

| Aliment      | Quantité |
|---|---|
| Riz          | 300g     |
| Œufs         | 196g     |
| Lentilles    | 205g     |
| Huile d'olive| 37g      |
| Pain complet | 300g     |

## Structure du projet
```
diete/
├── data/
│   ├── aliments.csv
│   └── besoins.csv
├── notebooks/
│   └── diete.ipynb
├── script/
│   └── script.py
└── README.md
```

## Outils
- Python 3.12
- PuLP
- GLPK
- pandas
