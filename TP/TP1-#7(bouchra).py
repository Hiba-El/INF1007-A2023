# Demande à l'utilisateur de saisir le nombre de secondes
s = int(input("Entrez le nombre de secondes: "))

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

# Affichage du nombre d'années, de semaines, de jours, d'heures, de minutes et de secondes
estAnneesNonNull   = annees >= 1
estSemainesNonNull = semaines >= 1
estJoursNonNull    = jours >= 1
estHeursNonNull    = heures >= 1
estMinutesNonNull  = minutes >= 1
affihcerResultat= ""

if estAnneesNonNull:
    affihcerResultat = affihcerResultat + str(annees)+" annees, "

if estSemainesNonNull:
    affihcerResultat = affihcerResultat + str(semaines)+" semaines, "

if estJoursNonNull:
    affihcerResultat = affihcerResultat + str(jours)+" jours, "

if estHeursNonNull:
    affihcerResultat = affihcerResultat + str(heures)+" heures, "

if estMinutesNonNull:
    affihcerResultat = affihcerResultat + str(minutes)+" minutes"

print("En", s, "secondes, on a:", affihcerResultat+" et", str(s_restantes)+" secondes.")
