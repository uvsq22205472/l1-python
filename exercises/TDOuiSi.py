# Le Chrono
import time
import keyboard
from win10toast import ToastNotifier

def NombreEnPluriel(nombre):
    '''Determine en fonction d'un nombre si une phrase associé doit comporter un s ou pas,
    à utiliser dans la fonction afficheTempsDeux
        Importée du module td3.py'''
    if nombre != 1:
        return 's'
    else:
        return ''


def afficheTemps(temps):
    '''Affiche affichage: un string avec le nombre de jours, heures, minutes et secondes en fonction de temps
    qui est un tuple contenant ces nombres.
        Importée du module td3.py et modifié pour ce module.'''
    affichage = ''
    TimeString  = ('J','Hr', 'Min', 'Sec' )
    for i in range(0,4):
        if temps[i] == 0:
            affichage += ('')
        else:
            affichage += (str(temps[i]) + ' ' + TimeString[i]+ ' ')
    return(affichage)


def secondesEnTemps(secondes):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument
        Importée du module td3.py"""
    
    tempsbrut = secondes / 216000
    jours = tempsbrut
    heures = (jours - int(jours)) * 60   
    minutes = (heures - int(heures)) * 60
    secondes = (minutes - int(minutes))* 60
    return (int(jours),int(heures),int(minutes),int(secondes))


def Chrono(temps):
    ''' Affiche un message lors du passage du temps ( en secondes ) , et affiche
    le temps restant tout les 5 secondes en secondes , en minutes et en heures.
    Pour faire le TD il faudrga convertir le temps nécessaire en secondes.
    4 min 12 sec => 252 sec '''
    # Affectation des variables
    temps_ecoule = 0
    toast = ToastNotifier()
    LineClear = "\x1b[2K"

    # Attente de l'utilisateur
    print('⇒ Cliquez sur la touche G pour commencer.', '\n','⇒ Attention à ne pas modifier le code.')
    while True:
        if keyboard.read_key() == "G" or keyboard.read_key() == 'g':
            break
    # Le countdown
    for i in range(0, temps):
        print('〓Temps restant = ', afficheTemps(secondesEnTemps(temps - temps_ecoule)),end= '● ')
        print('Temps écoulé = ', afficheTemps(secondesEnTemps(temps_ecoule)),'〓', end= "\r")
        time.sleep(1)
        temps_ecoule += 1
        print(end=LineClear)
    # Affichage de la notification Windows
    toast.show_toast("〓Chronomètre〓", "Le temps vient d'être écoulé. L'oeuf coque est prêt!",
    duration = 30, threaded = True, )
    return None

Chrono(60)