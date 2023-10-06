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

#13
def obtenir_etat(grille, ligne, colonne):
    etat = obtenir_case(grille,ligne,colonne)['etat']
    return etat
#14
def obtenir_animal(grille, ligne, colonne):
    # TODO: Retourner l'animal présent dans la case aux coordonnées données (ligne, col) (Dict)
    animal = obtenir_case(grille, ligne,colonne)['animal']
    return animal
#15
def definir_animal(grille, animal, ligne, col):
    # TODO: Placer un animal (sous forme de dictionnaire) sur la case indiquée par les coordonnées (ligne, col).
    grille['matrice'][ligne][col]['animal'] = animal
    return grille
##CMT ON UTILIE OBTENIR_ANIMAL PR PLACER DIRECTEMENT LANIMAL AU LIEU DE REFAIRE LE CHEMIN

#16
def definir_case(grille, case, ligne, col):
    grille['matrice'][ligne][col]= case
    return grille

#17
def vider_case(grille, ligne, col):
    # TODO: Écraser la case située à la ligne et la colonne données avec une case vide
    grille['matrice'][ligne][col] = creer_case()
    return grille

#18

def obtenir_population(grille):
    # TODO: Retourner un tuple contenant le nombre actuel de proies et de prédateurs dans la grille (Tuple[Int, Int])
    population = grille['nb_proies'], grille['nb_predateurs']
    return population

#19

def obtenir_dimensions(grille):
    # TODO: Retourner un tuple avec le nombre de lignes et de colonnes de la grille (Tuple[Int, Int])
    dimensions = grille['nb_lignes'], grille['nb_colonnes']
    return dimensions

#20
def incrementer_nb_proies(grille):
    # TODO: Augmenter le compteur du nombre de proies dans la grille de 1 (Int)
    grille['nb_proies'] +=1
    return grille

#21
def decrementer_nb_proies(grille):
    # TODO: Diminuer le compteur du nombre de proies dans la grille de 1 (Int)
    if grille['nb_proies'] != 0:
        grille['nb_proies'] -=1
    return grille

#22
def incrementer_nb_predateurs(grille):
    # TODO: Augmenter le compteur du nombre de prédateurs dans la grille de 1 (Int)
    grille['nb_predateurs'] +=1
    return grille
#23
def decrementer_nb_predateurs(grille):
    # TODO: Diminuer le compteur du nombre de prédateurs dans la grille de 1 (Int)
    if grille['nb_predateurs'] != 0:
        grille['nb_predateurs'] -=1
    return grille
#24
def check_nb_proies(grille, max_val):
    # TODO: Vérifier si le nombre actuel de proies dans la grille est inférieur à max_val (Booléen)
    if grille['nb_proies'] < max_val:
        return True
    elif grille['nb_proies'] >= max_val:
        return False
#25
def ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col):
    # TODO: Ajuster la position (ligne, colonne) pour une grille circulaire en utilisant les dimensions de la grille.
    # Indice: Un modulo (%) peut être utile.
    pass