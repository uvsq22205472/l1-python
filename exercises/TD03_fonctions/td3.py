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
    '''Affiche affichage: un string avec le nombre de jours, heures, minutes et secondes en fonction de temps
    qui est un tuple contenant ces nombres.'''
    affichage = ''
    TimeString  = ('jour','heure','minute','seconde')
    for i in range(0,4):
        affichage += (str(temps[i]) +' '+ TimeString[i]+NombreEnPluriel(temps[i])+' ')
    print(affichage)
    
afficheTempsDeux((3,13,23,1))
#####################################################"
# 
def DemandeTemps():
    '''La fonction demande à l'utilisateur de rentrer des nombres symbolisant des jours, heures, minutes et secondes
    (avec leurs restrictions) et envoi un tuple contenant cette combinaison pour pouvoir l'utiliser dans les autres 
    fonctions présentes dans ce fichier.'''
    
    DayCheck = ''
    HourCheck = ''
    MinuteCheck = ''
    SecondCheck = ''
    while DayCheck != True:
        Day = int(input('Donnez un nombre de jours compris entre 0 et 355'))
        if Day in range(0,356):
            DayCheck = True
        else:
            DayCheck = False
    while HourCheck != True:
        Hour = int(input("Donnez un nombre d'heures compris entre 0 et 23"))
        if Hour in range(0,24):
            HourCheck = True
        else:
            HourCheck = False
    while MinuteCheck != True:
        Minute = int(input('Donnez un nombre de minutes compris entre 0 et 59'))
        if Minute in range(0,60):
            MinuteCheck = True
        else:
            MinuteCheck = False
    while SecondCheck != True:
        Second = int(input('Donnez un nombre de secondes compris entre 0 et 59'))
        if Second in range(0,60):
                SecondCheck = True
        else:
                SecondCheck = False
    return((Day,Hour,Minute,Second))
    
afficheTempsDeux(DemandeTemps())
###################################################################
def SommeTemps(temps1, temps2):
    '''Convertit deux tuples supposés temps en secondes, puis fais la somme et reconvertit en tuples'''
    temps1 = tempsEnSecondes(temps1)
    temps2 = tempsEnSecondes(temps2)
    somme = temps1 + temps2
    return secondesEnTemps(somme)


print(SommeTemps((2,3,4,25),(5,22,57,1)))

def ProportionTemps(temps,proportion):
    """"""
    temps = tempsEnSecondes(temps)
    temps = ( temps * proportion )
    return secondesEnTemps(temps) 


afficheTemps(ProportionTemps((2,0,36,0),0.2))
###############################################################
def secondesEnDate(secondes):
    """Renvoie la date (annee, mois, jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    tempsbrut = secondes / 31536000
    annees = tempsbrut
    mois = (annees - int(annees)) * 12
    jours = (mois - int(mois)) * 30
    heures = (jours - int(jours)) * 60   
    minutes = (heures - int(heures)) * 60
    secondes = (minutes - int(minutes))* 60
    return (int(annees),int(mois),int(jours),int(heures),int(minutes),int(secondes))

def tempsEnDate(temps):
    """Prend le temps en secondes et le convertit en date a l'aide de secondesEnDate.
        Le temps 0 est le 1er janvier 1970 a 00:00:00
        La date finale est exprimee en:
        annees, mois, jours, heures, minutes et secondes."""
    # le temps 0 est le 1 janvier 1970 à 00:00:00.
    date = (1970,1,1,0,0,0)
    temps = secondesEnDate(temps)
    date = list(date)
    temps = list(temps)
    
    for i in range(0,5):
        date[i] = date[i] + temps[i]
    while date[5] > 60:
        date[5] -= 60
        date[4] += 1
    while date[4] > 60:
        date[4] -= 60
        date[3] += 1
    while date[3] > 24:
        date[3] -= 24
        date[2] += 1
    while date[2] > 30:
        date[3] -= 30
        date[2] += 1
    while date[1] > 30:
        date[1] -= 30
        date[0] += 1
    date = tuple(date)
    return(date))

tempsEnDate(31536000)

    

def afficheDate(date):
    