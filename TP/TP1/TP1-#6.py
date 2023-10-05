
# Demandez à l'utilisateur d'entrer son poids en kg
p = float(input("Entrez votre poids en kg: "))

# Demandez à l'utilisateur d'entrer sa taille en mètres
t = float(input("Entrez votre taille en m: "))

# Calculez l'Indice de Masse Corporelle (IMC) en utilisant la formule IMC = poids / (taille^2)
imc = p/(t**2)

# Affichez l'IMC avec une précision de deux décimales
print("Votre IMC est:", round(imc, 2))

# Définissez des conditions pour déterminer la catégorie de poids en fonction de l'IMC
# Si l'IMC est inférieur à 18.5, la personne est en sous-poids
estSousPoids = imc < 18.5

# Si l'IMC est inférieur à 24.9, la personne a un poids normal
estPoidsNormal = imc < 24.9

# Si l'IMC est inférieur à 30, la personne est en surpoids
estSurPoids = imc < 30

# Utilisez des instructions conditionnelles pour afficher la catégorie de poids
if estSousPoids:
    print("Vous etes en sous-poids.")

elif estPoidsNormal:
    print("Votre poids est normal.")

elif estSurPoids:
    print("Vous etes en surpoids.")

else:
    print("Vous etes obese.")
