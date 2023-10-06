from TP2_animal import creer_animal
from enum import Enum
import random
class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2
#10
def creer_case(etat=Contenu.VIDE, animal=None):
    # TODO: Créer et retourner un dictionnaire représentant une case.
    #  Utiliser les arguments pour initialiser l'état et l'animal dans la case.
    case = {}
    case["etat"] = etat
    case["animal"] = animal
    return case

#11

def creer_grille(nb_lignes, nb_colonnes):
    # TODO: Créer une matrice 2D de cases vides et la retourner sous forme de dictionnaire
    # TODO: Dans le dictionnaire, ajouter des métadonnées décrites dans l'énoncé (nombre de proies, de prédateurs, etc.)
    grille = {}
    lignes = []
    colonnes = []
    for i in range(nb_lignes):
        n = 0
        while n < nb_colonnes:
            n += 1
            colonnes.append(creer_case())
        lignes.append(colonnes)
        grille["matrice"] = lignes
    grille["nb_proies"] = 0
    grille["nb_predateurs"] = 0
    grille["nb_lignes"] = nb_lignes
    grille["nb_colonnes"] = nb_colonnes
    return grille

animal1 = creer_animal(age=5, energie=50)
animal2 = creer_animal(age=3, jrs_gestation=1, energie=30)
animal3 = creer_animal(age=2, disponible=False)

grille = creer_grille(2, 2)
grille["matrice"][0][0]["etat"] = Contenu.PROIE
grille["matrice"][0][0]["animal"] = animal1
grille["matrice"][1][1]["etat"] = Contenu.PREDATEUR
grille["matrice"][1][1]["animal"] = animal2
grille["matrice"][1][0]["etat"] = Contenu.PROIE
grille["matrice"][1][0]["animal"] = animal3
print(grille )