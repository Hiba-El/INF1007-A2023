# Demander à l'utilisateur de choisir le type de conversion
conversion = float(input("""Type de conversion :
1: Kilometres vers Miles (K vers M)
2: Miles vers Kilometres (M vers K)
Entrez votre choix (1 ou 2): """))

# Demande de la distance à l'utilisateur
distance = float(input("Entrez la distance a convertir: "))

# Vérifie si l'utilisateur a choisi la conversion de kilomètres en miles
choixKmEnMiles = conversion == 1

# Conversion de la distance en fonction du choix de l'utilisateur
if choixKmEnMiles:
    # Conversion de kilomètres en miles
    distance_M = distance * 0.621371
    # Affichage du résultat de la conversion
    print(distance, "kilometres equivalent a", round(distance_M, 2), "miles.")

else:
# Conversion de miles en kilomètres
    distance_K= distance / 0.621371
    # Affichage du résultat de la conversion
    print(distance, "miles equivalent a", round(distance_K, 2), "kilometres.")