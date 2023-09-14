import math

# Demander à l'utilisateur d'entrer les coefficients de l'équation quadratique

a = float(input("Veuillez entrer la valeur de a (coefficient de x^2):"))
b = float(input("Veuillez entrer la valeur de b (coefficient de x):"))
c = float(input("Veuillez entrer la valeur de c (terme constant):"))

# Calculer le discriminant

delta = math.sqrt((b**2)-(4*a*c))

# Vérifier si le discriminant est négatif (aucune racine réelle)
naPasDeSolution = delta <0

if naPasDeSolution:
    # Cette ligne de code sera exécutée si le projectile n'atteint jamais l'altitude désirée.
    print("Le projectile n'atteint jamais l'altitude desiree.")
else:
    # Vérifier si le discriminant est nul (une seule racine réelle)
    aUneSeuleSolution = delta == 0

    if aUneSeuleSolution:
        # Calculer l'instant unique où le projectile atteint l'altitude
        instant_unique = (-(b**2) + math.sqrt(delta)) / (2*a)

        # Vérifier si l'instant est positif
        estInstantPositif = instant_unique > 0
        if estInstantPositif:
            print(instant_unique)
            # Afficher l'instant
        else:
            # Afficher que le projectile n'atteint jamais l'altitude désirée.
            print("Le projectile n'atteint jamais l'altitude desiree.")
    else:
        # Calculer les deux instants où le projectile atteint l'altitude
        instant_1 =(-(b**2) + sqrt(delta)) / (2*a)
        instant_2 =(-(b**2) - sqrt(delta)) / (2*a)

        # Vérifier si les instants sont positifs
        estInstant1PositifInstant2Negatif = instant_1 > 0 and instant_2 < 0
        estInstant2PositifInstant1Negatif = instant_2 > 0 and instant_1 < 0
        estInstant1PositifInstant2Positif = instant_1 > 0 and instant_2 > 0

        if estInstant1PositifInstant2Negatif:

            # Afficher l'instant positif
            print("Instant de l'impact:", instant_1)

        elif estInstant2PositifInstant1Negatif:

            # Afficher l'instant positif
            print("Instant de l'impact:", instant_2)

        elif estInstant1PositifInstant2Positif:

            # Afficher les deux instants
            print("Instant de l'impact:", instant_1,"et",instant_2)

        else:
            # Afficher que le projectile n'atteint jamais l'altitude désirée.
            print("Le projectile n'atteint jamais l'altitude desiree")