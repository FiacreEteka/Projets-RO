# Problème du Voyageur de Commerce (TSP)

## Description
Un commercial basé à Paris doit visiter 5 villes françaises et revenir 
à Paris en minimisant la distance totale parcourue. Le problème est 
modélisé comme un TSP et résolu par programmation linéaire en nombres 
entiers avec les contraintes MTZ pour éliminer les sous-tours.

## Modèle mathématique

### Variables de décision
- **x_ij ∈ {0,1}** — 1 si on va directement de la ville i à la ville j
- **u_i ∈ {1,...,n-1}** — position de la ville i dans le tour (MTZ)

### Objectif
Minimiser la distance totale : Min Z = Σ_i Σ_j d_ij * x_ij

### Contraintes
- **Degré entrant** : chaque ville est visitée exactement une fois
- **Degré sortant** : chaque ville est quittée exactement une fois
- **MTZ** : u_i - u_j + n*x_ij ≤ n-1 — élimination des sous-tours
- **Domaine** : x_ij ∈ {0,1}, u_i entier

## Résultats

**Tour optimal :**