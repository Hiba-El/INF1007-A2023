# Demande à l'utilisateur d'entrer une phrase.
phrase = input("Entrez une phrase:")

# Divise la phrase en mots en utilisant l'espace comme séparateur et compte le nombre de mots

nombre_mots = len(str.split(phrase))


# Affiche le nombre de mots dans la phrase

print("Le nombre de mots est:",nombre_mots)

# Affiche la phrase en lettres majuscules

print(phrase.upper())
