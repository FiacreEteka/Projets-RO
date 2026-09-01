# Projets en Recherche Opérationnelle

Collection de projets de modélisation et résolution de problèmes 
d'optimisation réalisés en Master 1.

## Projets

### 1. [Problème de Transport](./transport/)
Minimisation du coût de transport entre 3 entrepôts et 4 magasins.
- **Outils** : PuLP, GLPK, pandas
- **Méthode** : Programmation linéaire
- **Variables** : Continues

### 2. [Problème de Diète](./diète/)
Composition d'un menu journalier au coût minimum sous contraintes nutritionnelles.
- **Outils** : PuLP, GLPK, pandas
- **Méthode** : Programmation linéaire
- **Variables** : Continues

### 3. [Problème du Sac à Dos](./sac-a-dos/)
Sélection d'objets à emporter dans un sac à dos pour maximiser la valeur totale.
- **Outils** : OR-Tools CP-SAT, pandas
- **Méthode** : Programmation en nombres entiers
- **Variables** : Binaires

### 4. [Coloration de Graphe](./coloration-graphe/)
Planning d'examens avec nombre minimum de créneaux.
- **Outils** : OR-Tools CP-SAT, NetworkX, Matplotlib
- **Méthode** : Programmation en nombres entiers
- **Variables** : Binaires

## Compétences mobilisées
- Modélisation mathématique (variables, fonction objectif, contraintes)
- Programmation linéaire et en nombres entiers
- Python : PuLP, OR-Tools, pandas
- Scripts Python structurés en fonctions
- Gestion de version : Git / GitHub

### 5. [Problème du Voyageur de Commerce (TSP)](./tsp/)
Tour optimal passant par 6 villes françaises avec contraintes MTZ.
- **Outils** : PuLP, GLPK, pandas
- **Méthode** : PLNE + contraintes MTZ
- **Variables** : Binaires + entières

### 6. [Problème de Tournées de Véhicules (VRP)](./vrp/)
Optimisation de 3 tournées de livraison dans 10 villes françaises.
- **Outils** : PuLP, GLPK, pandas
- **Méthode** : PLNE + contraintes MTZ + conservation de flux
- **Variables** : Binaires + entières

### 7. [Réseau de Distribution Humanitaire](./humanitaire/)
Optimisation de l'aide humanitaire après une inondation au Bénin.
- **Outils** : Pyomo, GLPK, pandas, folium
- **Méthode** : PLNE mixte (variables binaires + continues)
- **Impact** : Analyse de sensibilité sur le nombre de dépôts

### 8. [Chaîne logistique agricole](./agricole/)
Maximisation du profit d'une coopérative agricole sous contraintes de 
production, demande et pertes post-récolte. Comparaison de trois 
approches : solveur exact, heuristique gloutonne et algorithme génétique.
- **Outils** : PuLP, algorithmes génétiques, pandas
- **Méthode** : PLNE + heuristique + métaheuristique (analyse comparative)

### 9. [Prédiction de la Consommation Énergétique & Allocation de Ressources](./prevision-energie/)
Régression supervisée (Temperature, HVACUsage, Occupancy) combinée à 
une optimisation d'allocation de budget énergétique sous contrainte. 
- **Outils** : scikit-learn, PuLP, pandas, statsmodels
- **Méthode** : régression linéaire/Random Forest + PLNE binaire (allocation de ressources)

## Auteur
Fiacre Eteka — Master 1
