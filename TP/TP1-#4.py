
# Affiche un menu d'opérations disponibles

print("""Choisissez une operation:
    1. Addition
    2. Soustraction
    3. Multiplication
    4. Division""")

# Demande à l'utilisateur de saisir le numéro de l'opération choisie
operation = int(input(""))

# Demande à l'utilisateur de saisir deux nombres
premier_nombre= float(input("Entrez le premier nombre: "))
deuxieme_nombre= float(input("Entrez le second nombre: "))

# Vérifie si l'opération choisie correspond à l'addition
estAddition = 1
# Vérifie si l'opération choisie correspond à la soustraction
estSoustraction = 2
# Vérifie si l'opération choisie correspond à la multiplication
estMultiplication = 3
# Vérifie si l'opération choisie correspond à la division
estDivision = 4


# Si l'opération choisie est l'addition, affiche le résultat de l'addition
if operation == estAddition:
    print("Resultat:",premier_nombre+deuxieme_nombre)

# Si l'opération choisie est la soustraction, affiche le résultat de la soustraction
elif operation == estSoustraction:
    print("Resultat:",premier_nombre-deuxieme_nombre)

# Si l'opération choisie est la multiplication, affiche le résultat de la multiplication
elif operation == estMultiplication:
    print("Resultat:",premier_nombre * deuxieme_nombre)

# Si l'opération choisie est la division
elif operation == estDivision:
    # Vérifie si la division par zéro est tentée
    conditionDivisionZero = deuxieme_nombre == 0
    # Si la division par zéro est tentée, affiche une erreur
    if conditionDivisionZero:
        print("Erreur: Division par zero.")

    # Sinon, affiche le résultat de la division
    else:
        print("Resultat:",premier_nombre / deuxieme_nombre)
# Si l'opération choisie n'est pas valide, affiche un message d'erreur
else:
    print("Operation non-valide!")

