#1

def creer_animal(age=0, jrs_gestation=0, energie=15, disponible=True):
    # TODO: Créer et retourner un dictionnaire représentant un animal.
    #  Utiliser les arguments de la fonction pour initialiser les valeurs.
    animal = {}
    animal["age"] = age
    animal["jrs_gestation"] = jrs_gestation
    animal["energie"] = energie
    animal["disponible"] = disponible
    return animal
animal = (creer_animal(5,10,100,False))
#print(animal)
#2

def obtenir_age(animal):
    # TODO: Retourner la valeur de l'âge de l'animal donné (Int)
    return int(animal["age"])

#print(obtenir_age(animal))

#3

def obtenir_jours_gestation(animal):
    # TODO: Retourner le nombre de jours de gestation de l'animal donné (Int)
    return int(animal["jrs_gestation"])

#4

def obtenir_energie(animal):
# TODO: Retourner la quantité d'énergie de l'animal donné (Int)
    return int(animal["energie"])

#5

def obtenir_disponibilite(animal):
    # TODO: Retourner l'état de disponibilité de l'animal (Booléen)
    return bool(animal["disponible"])

#6

def incrementer_age(animal, puberte):
    # TODO: Incrémenter l'âge de l'animal de 1
    animal["age"] += 1
    # TODO: Si l'animal est plus âgé que l'âge de la puberté, incrémenter son nombre de jours de gestation de 1
    if animal["age"] >= puberte:
        animal["jrs_gestation"] += 1

#7

def definir_jours_gestation(animal, jrs_gest):
    # TODO: Mettre à jour le nombre de jours de gestation de l'animal avec la valeur jrs_gest donnée (Int)
    animal["jrs_gestation"] = jrs_gest

#8

def ajouter_energie(animal, valeur):
    # TODO: Ajouter la quantité d'énergie donnée (valeur) à l'énergie actuelle de l'animal (Int)
    animal["energie"] += valeur
#9

def definir_disponibilite(animal, disponibilite):
    # TODO: Mettre à jour l'état de disponibilité de l'animal en utilisant le paramètre permis (Booléen)
    animal["disponible"] = disponibilite