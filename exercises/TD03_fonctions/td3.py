#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes


from pickle import NONE


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

#####################################################
def afficheTemps(temps):
    """Affiche le(s) jour(s) , le(s) heure(s) , minute(s), seconde(s) à partir d'un temps uniquement
    end secondes."""

    if temps[0] == 1:
        print(temps[0],' jour')
    else:
        print(temps[0],' jours')
    if temps[1] == 1:
        print(temps[1],' heure')
    else:
        print(temps[1],' heures')
    if temps[2] == 1:
        print(temps[2],' minute')
    else:
        print(temps[2],' minutes')
    if temps[3] == 1:
        print(temps[3],' seconde')
    else:
        print(temps[3],' secondes')
afficheTemps((3,13,23,1))
def NombreEnPluriel(nombre):
    '''Determine en fonction d'un nombre si une phrase associé doit comporter un s ou pas,
    à utiliser dans la fonction afficheTempsDeux'''
    if nombre != 1:
        return 's'
    else:
        return ''
    
def afficheTempsDeux(temps):
    affichage = ''
    affichagetemps = ('jour','heure','minute','seconde')
    for i in range(0,4):
        affichage += (str(temps[i]) +' '+ affichagetemps[i]+NombreEnPluriel(temps[i])+' ')
    print(affichage)
    
afficheTempsDeux((3,13,23,1))

def DemandeTemps()
    temps = 