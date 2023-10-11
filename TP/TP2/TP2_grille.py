from TP2_animal import creer_animal
from TP2_animal import obtenir_disponibilite
from enum import Enum
import random
class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2
#10
def creer_case(etat=Contenu.VIDE, animal=None):
    # : Créer et retourner un dictionnaire représentant une case.
    #  Utiliser les arguments pour initialiser l'état et l'animal dans la case.
    case = {}
    case["etat"] = etat
    case["animal"] = animal
    return case

#11

def creer_grille(nb_lignes, nb_colonnes):
    # : Créer une matrice 2D de cases vides et la retourner sous forme de dictionnaire
    grille={}
    colonnes=[]
    #: Dans le dictionnaire, ajouter des métadonnées décrites dans l'énoncé (nombre de proies, de prédateurs, etc.)
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
    # :
    case = grille['matrice'][ligne][colonne]
    return case

#13
def obtenir_etat(grille, ligne, colonne):
    etat = obtenir_case(grille,ligne,colonne)['etat']
    return etat
#14
def obtenir_animal(grille, ligne, colonne):
    # : Retourner l'animal présent dans la case aux coordonnées données (ligne, col) (Dict)
    animal = obtenir_case(grille, ligne,colonne)['animal']
    return animal
#15
def definir_animal(grille, animal, ligne, col):
    # : Placer un animal (sous forme de dictionnaire) sur la case indiquée par les coordonnées (ligne, col).
    grille['matrice'][ligne][col]['animal'] = animal
    return grille
##CMT ON UTILIE OBTENIR_ANIMAL PR PLACER DIRECTEMENT LANIMAL AU LIEU DE REFAIRE LE CHEMIN

#16
def definir_case(grille, case, ligne, col):
    grille['matrice'][ligne][col]= case
    return grille

#17
def vider_case(grille, ligne, col):
    # : Écraser la case située à la ligne et la colonne données avec une case vide
    grille['matrice'][ligne][col] = creer_case()
    return grille

#18

def obtenir_population(grille):
    # : Retourner un tuple contenant le nombre actuel de proies et de prédateurs dans la grille (Tuple[Int, Int])
    population = grille['nb_proies'], grille['nb_predateurs']
    return population

#19

def obtenir_dimensions(grille):
    # : Retourner un tuple avec le nombre de lignes et de colonnes de la grille (Tuple[Int, Int])
    dimensions = grille['nb_lignes'], grille['nb_colonnes']
    return dimensions

#20
def incrementer_nb_proies(grille):
    # : Augmenter le compteur du nombre de proies dans la grille de 1 (Int)
    grille['nb_proies'] +=1
    return grille

#21
def decrementer_nb_proies(grille):
    # : Diminuer le compteur du nombre de proies dans la grille de 1 (Int)
    if grille['nb_proies'] != 0:
        grille['nb_proies'] -=1
    return grille

#22
def incrementer_nb_predateurs(grille):
    # : Augmenter le compteur du nombre de prédateurs dans la grille de 1 (Int)
    grille['nb_predateurs'] +=1
    return grille
#23
def decrementer_nb_predateurs(grille):
    # : Diminuer le compteur du nombre de prédateurs dans la grille de 1 (Int)
    if grille['nb_predateurs'] != 0:
        grille['nb_predateurs'] -=1
    return grille
#24
def check_nb_proies(grille, max_val):
    # : Vérifier si le nombre actuel de proies dans la grille est inférieur à max_val (Booléen)
    if grille['nb_proies'] < max_val:
        return True
    elif grille['nb_proies'] >= max_val:
        return False
#25
def ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col):
    # : Ajuster la position (ligne, colonne) pour une grille circulaire en utilisant les dimensions de la grille.
    # Indice: Un modulo (%) peut être utile.
    if col >= dim_col:  #à droite
        col = col % dim_col
    elif col < 0: #à gauche
        col = col % dim_col
    if lig >= dim_lig: #en bas
        lig = lig % dim_lig
    elif lig < 0: #en haut
        lig = lig % dim_lig
    return (lig, col)

#26
def choix_voisin_autour(grille, ligne, col, contenu: Contenu):
    # Chercher tous les voisins autour de la cellule (ligne, col) qui correspondent au "contenu" donné (Enum).
    # Renvoyer le nombre total de ces voisins, ainsi que les coordonnées d'un voisin choisi aléatoirement (Tuple).
    # Si le contenu n'est pas VIDE, le voisin doit être disponible (voir la fonction obtenir_disponibilite).
    # Indice: Utiliser la fonction "ajuster_position_pour_grille_circulaire" pour ajuster les positions des voisins qui sont en dehors de la grille.
    lig_voisin = None
    lig_colonne = None
    tabcases = []
    nb_lig, nb_col = obtenir_dimensions(grille)
    for i in range(ligne-1, ligne+1):
        for j in range(col-1, col+1):
            if i != ligne or j != col:
                i2, j2 = ajuster_position_pour_grille_circulaire(ligne, col, nb_lig, nb_col)
                animal = obtenir_animal(grille, i2, j2)
                if obtenir_etat(grille, i2, j2) == contenu:
                    if contenu == Contenu.VIDE or obtenir_disponibilite(animal) is False:
                        tabcases.append(i2)
                        tabcases.append(j2)
    if not tabcases.count:
        lig_voisin = random
        col_voisin = random
        return tabcases.count, lig_voisin, col_voisin
    else:
        return tabcases.count, None, None

