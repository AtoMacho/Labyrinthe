# Générateur de Labyrinthes et Exportateur 3D
Ce projet implémente deux algorithmes de génération de labyrinthes et exporte les labyrinthes générés au format ```.scad```, compatible avec OpenSCAD pour la visualisation et l'impression 3D.

## Fonctionnalités
- Algorithmes de génération de labyrinthes :
  - Algorithme 1 : Recherche en profondeur (Depth-First Search - DFS)
  - Algorithme 2 : Algorithme de Kruskal
    
- Exportation en 3D :
  - Les labyrinthes sont sauvegardés au format ```.scad```, prêts à être visualisés ou imprimés en 3D.
  - Inclut des paramètres personnalisables tels que la taille des cellules, la hauteur et l'épaisseur des murs.
  - Ajoute une identification du cours (```IFT2125```) et les initiales dans le labyrinthe généré.

## Prérequis
- Python 3.12 ou version ultérieure.
- OpenSCAD pour visualiser et rendre les fichiers ```.scad```.

## Utilisation
Exécutez le script avec le numéro de l'algorithme souhaité en paramètre :

```
python3 labyrinth_generator_creator.py 1
```
ou

```
python3 labyrinth_generator_creator.py 2
```

## Paramètres
- Algorithme 1 : Utilise la recherche en profondeur (DFS) pour générer le labyrinthe.
- Algorithme 2 : Utilise l'algorithme de Kruskal pour générer le labyrinthe.

## Résultat
Le script génère un fichier ```.scad``` nommé ```labyrinthe_algoX.scad```, où ```X``` correspond au numéro de l'algorithme sélectionné (1 ou 2).

## Exemple de Résultat
Une fois le script exécuté, vous pouvez utiliser OpenSCAD pour visualiser le modèle 3D du labyrinthe.

## Personnalisation
Les paramètres suivants peuvent être ajustés directement dans le script :

- ```cell_size``` : Dimensions de chaque cellule du labyrinthe en millimètres.
- ```wall_height``` : Hauteur des murs en millimètres.
- ```wall_thickness``` : Épaisseur des murs en millimètres.
- ```floor_thickness``` : Épaisseur du sol en millimètres.

## Fonctionnalité Bonus
Pour obtenir des points supplémentaires, le labyrinthe généré peut être imprimé en 3D en respectant les consignes suivantes :

- Dimensions : 8–12 cm × 8–12 cm avec des murs de 0.8–1.2 cm de hauteur.
- Doit inclure le code du cours (```IFT2125```) et les initiales (```LK``` et ```SF```) dans le modèle 3D.

## Auteurs
- Lucky Khounvongsa (20172476)
- Salim Fathya (20210127)
