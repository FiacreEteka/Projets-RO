# Prédiction de la Consommation Énergétique & Allocation de Ressources

## Description
Ce projet combine **data science** et **recherche opérationnelle** pour 
étudier la consommation énergétique d'un bâtiment. Il se déroule en deux 
temps : une phase de prévision par apprentissage supervisé, puis une 
phase d'optimisation exploitant les prédictions du modèle pour allouer 
un budget énergétique limité entre plusieurs bâtiments.


## Partie 1  Analyse exploratoire (EDA)

Étude statistique complète du jeu de données (1000 observations 
horaires) : distributions, corrélations de Pearson, tests ANOVA sur 
les variables catégorielles, et analyse d'autocorrélation (ACF).

**Résultats clés :**
- La **température** est le facteur dominant (r = 0.70, p < 0.001)
- **HVACUsage** est le facteur catégoriel le plus significatif (ANOVA F = 89.22)
- **SquareFootage** et **DayOfWeek** n'ont aucun effet significatif
- **Absence d'autocorrélation** temporelle (ACF) justifie une approche 
  de régression classique plutôt qu'une méthode de série temporelle

## Partie 2 Modélisation prédictive

Deux modèles de régression supervisée ont été comparés pour prédire 
`EnergyConsumption` à partir des variables environnementales et 
d'usage :

| Modèle | MAE | R² |
|---|---|---|
| Régression Linéaire | 4.11 | 0.598 |
| Random Forest | 4.38 | 0.545 |

**Importance des variables (Random Forest) :**
```
Temperature       58.3 %
RenewableEnergy    8.7 %
SquareFootage      7.9 %
Humidity           7.4 %
Occupancy          7.3 %
HVACUsage_On       7.2 %
LightingUsage_On   1.4 %
Holiday_Yes        0.9 %
DayOfWeek_Weekend  0.8 %
```

## Partie 3  Optimisation : allocation de ressources énergétiques

### Contexte
Une entreprise gérant plusieurs bâtiments dispose d'un **budget 
énergétique limité** à répartir pour l'activation du chauffage/
climatisation (HVAC). Les consommations prédites par le modèle de 
régression sont utilisées comme paramètres d'entrée d'un problème 
d'allocation sous contrainte.

### Modèle mathématique

**Variables de décision**
$$x_i \in \{0,1\} \quad \text{activer le HVAC dans le bâtiment } i$$

**Fonction objectif** maximiser le confort total des occupants
$$\max Z = \sum_{i} confort_i \cdot x_i$$

**Contrainte de budget**
$$\sum_{i} c_i \cdot x_i \leq B$$

où $c_i$ est la consommation prédite du bâtiment $i$ et $B$ le budget 
énergétique disponible (fixé à 60 % du besoin total, créant un 
arbitrage réel entre bâtiments).

### Résultat
Le solveur PuLP sélectionne, parmi 15 bâtiments échantillonnés, ceux à 
activer en priorité selon leur rapport confort/consommation, 
respectant strictement la contrainte budgétaire tout en maximisant le 
confort total des occupants.


## Structure du projet
```
prevision-energie/
├── data/
│   └── Energy_consumption.csv
├── notebooks/
│   └── prediction_consommation.ipynb
├── docs/
│   └── EDA_consommation_energetique.md
└── README.md
```

## Outils
- Python 3.12
- pandas, NumPy
- scikit-learn (LinearRegression, RandomForestRegressor)
- scipy (tests de Pearson et ANOVA)
- statsmodels (autocorrélation)
- matplotlib, seaborn
- PuLP (optimisation)

## Source des données
[Energy Consumption Prediction — Kaggle](https://www.kaggle.com/datasets/mrsimple07/energy-consumption-prediction)
