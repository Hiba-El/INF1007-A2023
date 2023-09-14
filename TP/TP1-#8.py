# Demander à l'utilisateur de choisir le type de conversion
conversion = float(input("""Choisir le type de conversion
1: Kilometres vers Miles (K vers M)
2: Miles vers Kilometres (M vers K)
Entres votre choix (1 ou 2):"""))

# Demande de la distance à l'utilisateur
distance = float(input("Entrez la distance a convertir:"))

# Vérifie si l'utilisateur a choisi la conversion de kilomètres en miles
choixKmEnMiles = conversion == 1

# Conversion de la distance en fonction du choix de l'utilisateur
if choixKmEnMiles:
    distance_M = distance * 0.621371
    print(distance, "kilometres equivalent a", round(distance_M, 2), "miles.")
# Conversion de kilomètres en miles
# Affichage du résultat de la conversion

else:
# Conversion de miles en kilomètres
    distance_K= distance / 0.621371
    print(distance, "miles equivalent a", round(distance_K, 2), "kilometres.")
# Affichage du résultat de la conversion
