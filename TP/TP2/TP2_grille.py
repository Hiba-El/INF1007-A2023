from TP2_animal import creer_animal
from TP2_animal import obtenir_disponibilite
from TP2_animal import obtenir_energie
from TP2_animal import obtenir_age
from TP2_animal import obtenir_jours_gestation
from TP2_animal import definir_jours_gestation
from TP2_animal import ajouter_energie
from enum import Enum
import random
class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2

NB_LIGNE = 25
NB_COLONNE = 50

MAX_AGE_PRED = 2000
NB_JRS_PUBERTE_PRED = 90
NB_JRS_GESTATION_PRED = 30
MIN_SANTE_PRED = 0
AJOUT_ENERGIE = 3
MIN_ENERGIE = 15

MAX_AGE_PROIE = 100
NB_JRS_PUBERTE_PROIE = 15
NB_JRS_GESTATION_PROIE = 9
NB_MAX_PROIES = NB_LIGNE * NB_COLONNE / 2
POURCENTAGE_CASES_PROIES = 0.5
POURCENTAGE_CASES_PREDATEURS = 0.05

MAX_ITERATION = 10000
DUREE_CYCLE = 500  # Millisecondes
DUREE_AVANT_REDEMARRAGE = 5000  # Millisecondes
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
    grille['matrice'] = colonnes
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
    col_voisin = None
    tabcases = []
    nb_lig, nb_col = obtenir_dimensions(grille)
    for i in range(ligne-1, ligne+2):
        for j in range(col-1, col+2):
            if i != ligne or j != col:
                i2, j2 = ajuster_position_pour_grille_circulaire(i, j, nb_lig, nb_col)
                animal = obtenir_animal(grille, i2, j2)
                if obtenir_etat(grille, i2, j2) == contenu:
                    if contenu == Contenu.VIDE or obtenir_disponibilite(animal):
                        paire = i2, j2
                        tabcases.append(paire)
    if len(tabcases) != 0:
        lig_voisin, col_voisin = random.choice(tabcases)
        return len(tabcases), lig_voisin, col_voisin
    else:
        return len(tabcases), None, None

#27
def remplir_grille(grille, pourcentage_proie, pourcentage_predateur):
    nb_lignes, nb_col = obtenir_dimensions(grille)
    nb_total_cases = int(nb_lignes*nb_col)
    nb_proies = int(pourcentage_proie*nb_total_cases)
    nb_predateurs = int(pourcentage_predateur*nb_total_cases)
    positions_possibles = []
    for i in range(nb_lignes):
        for j in range(nb_col):
            paire = i, j
            positions_possibles.append(paire)
    random.shuffle(positions_possibles)
    for i in range(nb_proies):
        position_proie = random.choice(positions_possibles)
        age_proie = random.randint(0, MAX_AGE_PROIE)
        if age_proie > NB_JRS_PUBERTE_PROIE:
            jours_gestation = random.randint(0, NB_JRS_GESTATION_PROIE)
        else:
            jours_gestation = 0
        case = creer_case()
        proie = creer_animal()
        case['animal'] = proie
        case['animal']['age'] = age_proie
        definir_jours_gestation(proie, jours_gestation)
        definir_case(grille, case, position_proie[0], position_proie[1])
        grille['nb_proies'] = nb_proies
    for i in range(nb_predateurs):
        position_predateur = random.choice(positions_possibles)
        age_pred = random.randint(0, MAX_AGE_PRED)
        if age_pred > NB_JRS_PUBERTE_PRED:
            jours_gestation_pred = random.randint(0, NB_JRS_GESTATION_PRED)
        else:
            jours_gestation_pred = 0
        case_pred = creer_case()
        predateur = creer_animal()
        case_pred['animal'] = predateur
        case_pred['animal']['age'] = age_pred
        definir_jours_gestation(predateur, jours_gestation_pred)
        ajouter_energie(predateur, AJOUT_ENERGIE)
        definir_case(grille, case_pred, position_predateur[0], position_predateur[1])
        grille['nb_predateurs'] = nb_predateurs
    return grille

#28
def rendre_animaux_disponibles(grille):
    # TODO: Parcourir chaque case de la grille et rendre tous les animaux disponibles (Booléen à True) pour la prochaine itération.
    pass
