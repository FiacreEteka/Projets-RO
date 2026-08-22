# Optimisation d'un Réseau de Distribution Humanitaire

## Contexte
Suite à une inondation au Bénin, une organisation humanitaire doit 
acheminer des secours vers 10 zones sinistrées depuis des dépôts 
stratégiquement localisés. L'objectif est de minimiser le coût total 
(ouverture des dépôts + transport) tout en satisfaisant la demande 
de chaque zone.

## Modèle mathématique

### Paramètres
- **f_i** — coût fixe d'ouverture du dépôt i
- **c_ij** — coût de transport du dépôt i vers la zone j
- **d_j** — demande de la zone sinistrée j (tonnes)
- **cap_i** — capacité maximale du dépôt i
- **M** — nombre maximum de dépôts à ouvrir

### Variables de décision
- **y_i ∈ {0,1}** — 1 si le dépôt i est ouvert, 0 sinon
- **x_ij ≥ 0** — quantité de secours (tonnes) envoyée du dépôt i vers la zone j

### Objectif
Min Z = Σ_i f_i * y_i + Σ_i Σ_j c_ij * x_ij

### Contraintes
- **Demande** : chaque zone sinistrée reçoit exactement sa demande
- **Liaison** : on ne livre depuis i que si le dépôt i est ouvert
- **Capacité** : la livraison totale depuis i ≤ capacité de i
- **Nombre** : au plus M dépôts ouverts
- **Budget** : montant à ne pas excéder 

## Résultats

### Analyse de sensibilité

| Scénario | Dépôts ouverts | Coût total | Gain marginal |
|---|---|---|---|
| M=3 | Parakou, Abomey, Natitingou | 5 620 420 FCFA | — |
| M=4 | + Cotonou | 4 905 602 FCFA | -714 818 FCFA |
| M=5 | + Porto-Novo | 4 905 602 FCFA | 0 FCFA |

### Conclusion
Le nombre optimal de dépôts est **4**. Au-delà, ouvrir des dépôts 
supplémentaires n'apporte aucun bénéfice économique.

### Solution optimale (M=4)
| Dépôt | Zones desservies | Charge |
|---|---|---|
| Parakou | Kandi, Bembéréké, Nikki, Savalou, Bohicon | 335/400 t |
| Abomey | Bohicon, Lokossa, Ouidah, Comè | 300/300 t |
| Natitingou | Malanville, Kandi, Djougou | 250/250 t |
| Cotonou | Ouidah, Comè | 130/500 t |

## Structure du projet
œuvre_humanitaire/
├── data/
│ ├── depots.csv
│ ├── zones.csv
│ ├── distances.csv
│ ├── couts_transport.csv
│ └── parametres.csv
├── notebook/
│ └── humanitaire.ipynb
├── outputs/
│ └── carte_humanitaire.html
| └── solution M=4
├── script/
|└── script.py
└── README.md

## Outils
- Python 3.12
- Pyomo
- GLPK
- pandas
- folium (visualisation carte)