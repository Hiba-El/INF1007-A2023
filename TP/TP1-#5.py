
# Demande à l'utilisateur d'entrer le montant initial de l'investissement

p = float(input("Entrez le montant initial:"))

# Demande à l'utilisateur d'entrer le taux d'intérêt annuel en pourcentage


r = float(input("Entrez le taux d'intérêt annuel (en %):"))

# Demande à l'utilisateur d'entrer le nombre d'années de l'investissement

t = float(input("Entrez le nombre d'années de l'investissement:"))

# Calcule le montant final en utilisant la formule de l'intérêt composé

a = p*(1+(r/100))**t

# Affiche le montant final avec deux décimales
print(round(a, 2))