# premiers nombres
# n = 3
# n1 = 3 x 3 + 1  = 10
# n2 = 10 / 2 = 5
# n3 = 5 x 3 + 1 = 16
# n4 = 16 / 2 = 8
# n5 = 8 / 2 = 4

def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    i = 0
    ListeSyracuse = [n]
    while ListeSyracuse[i] != 1 :
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        i += 1
        ListeSyracuse.append(n)
    return ListeSyracuse
print(syracuse(3))
def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    Conjecture = True
    for i in range(1,n_max):
        if syracuse(i)[-1] != 1:
            Conjecture = False
    return Conjecture

print(testeConjecture(30))

def tempsVol(n):
    ''' Retourne le temps de vol de n '''
    return (len(syracuse(n)) - 1)

print(tempsVol(1))
print(tempsVol(3))
print(tempsVol(100))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    VolListe = []
    for i in range(1,n_max):
        VolListe.append(tempsVol(i))
    return VolListe

print(tempsVolListe(100))