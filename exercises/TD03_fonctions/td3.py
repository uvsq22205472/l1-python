#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes


def tempsEnSecondes(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    Resultat = temps[0]*60**3 + temps[1]*60**2 + temps[2]*60 + temps[3]
    return Resultat


temps = (3,23,1,34)
print(type(temps))
print(tempsEnSecondes(temps))  

############
def secondesEnTemps(secondes):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    tempsbrut = secondes / 216000
    jours = tempsbrut
    heures = (jours - int(jours)) * 60   
    minutes = (heures - int(heures)) * 60
    secondes = (minutes - int(minutes))* 60
    return (int(jours),int(heures),int(minutes),int(secondes))


print(secondesEnTemps(tempsEnSecondes(temps)))