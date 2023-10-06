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
    grille={}
    colonnes=[]
    #TODO: Dans le dictionnaire, ajouter des métadonnées décrites dans l'énoncé (nombre de proies, de prédateurs, etc.)
    for i in range(nb_lignes):
        lignes=[]
        for n in range(nb_colonnes):
            lignes.append(creer_case())
        colonnes.append(lignes)
    grille['matrice']= colonnes
    grille['nb_proies'] = 0
    grille['nb_predateurs'] = 0
    grille['nb_lignes'] = nb_lignes
    grille['nb_colonnes'] = nb_colonnes
    return grille

#12
def obtenir_case(grille, ligne, colonne):
    # TODO:
    case = grille['matrice'][ligne][colonne]
    return case

