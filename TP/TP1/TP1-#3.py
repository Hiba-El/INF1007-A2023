# Demande à l'utilisateur d'entrer une phrase.
phrase = input("Entrez une phrase: ")

# Divise la phrase en mots en utilisant l'espace comme séparateur et compte le nombre de mots
nombre_mots = len(str.split(phrase))

# Affiche le nombre de mots dans la phrase
print("La phrase contient",nombre_mots, "mots.")

# Affiche la phrase en lettres majuscules
print("Phrase en majuscules:", phrase.upper())
