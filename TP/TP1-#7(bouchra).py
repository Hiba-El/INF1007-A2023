# Demande à l'utilisateur de saisir le nombre de secondes
s = float(input("Entrez le nombre de secondes:"))

# Calcul du nombre d'années contenant ces secondes (en supposant une année de 365 jours)
annees = s // 31536000
s_restantes = s - 31536000*annees

# Calcul du nombre de semaines restantes dans le reste des secondes
semaines = s_restantes // 604800
s_restantes = s_restantes - 604800*semaines

# Calcul du nombre de jours restants dans le reste des secondes
jours = s_restantes // 86400
s_restantes = s_restantes - 86400*jours

# Calcul du nombre d'heures restantes dans le reste des secondes
heures = s_restantes // 3600
s_restantes = s_restantes - 3600*heures

# Calcul du nombre de minutes restantes dans le reste des secondes
minutes = s_restantes // 60
s_restantes = s_restantes - 60*minutes
print("En", s, ",on a:")

# Affichage du nombre d'années, de semaines, de jours, d'heures, de minutes et de secondes
estAnneesNonNull   = annees >= 1
estSemainesNonNull = semaines >= 1
estJoursNonNull    = jours >= 1
estHeursNonNull    = heures >= 1
estMinutesNonNull  = minutes >= 1

if estAnneesNonNull:
    print(annees, "annees,")

if estSemainesNonNull:
    print(semaines, "semaines,")

if estJoursNonNull:
    print(jours, "jours,")

if estHeursNonNull:
    print(heures, "heures,")

if estMinutesNonNull:
    print(minutes, "minutes et", s_restantes, "secondes.")
