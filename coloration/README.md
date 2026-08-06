# Coloration de Graphe — Planning d'Examens

## Description
Une université doit planifier 8 examens en minimisant le nombre de créneaux 
horaires. Deux matières ayant des étudiants en commun ne peuvent pas être 
programmées au même créneau. Ce problème est modélisé comme une coloration 
de graphe.

## Modèle mathématique
- **Variables** :
  - x_ij ∈ {0,1} — 1 si la matière i est affectée au créneau j
  - y_j ∈ {0,1} — 1 si le créneau j est utilisé
- **Objectif** : Minimiser le nombre de créneaux utilisés
- **Contraintes** :
  - Chaque matière est affectée à exactement un créneau
  - Deux matières en conflit ne partagent pas le même créneau
  - Un créneau est activé si au moins une matière y est affectée

## Résultats
| Créneau | Matières |
|---|---|
| Créneau 0 | Maths, BDD, SVT |
| Créneau 1 | Physique, Algo, Anglais |
| Créneau 2 | Info, Chimie |

**Nombre minimum de créneaux : 3**

## Structure du projet
coloration-graphe/
├── notebooks/
│   └── coloration.ipynb
└── README.md

## Outils
- Python 3.12
- OR-Tools CP-SAT
- NetworkX
- Matplotlib
