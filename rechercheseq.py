from random import randrange
import time

T = []
def genereTableau(n):
    global T
    for i in range(n):
        T.append(randrange(0,10000))
        T = sorted(T)

def rechercheSeq(T,k):
    pos = -1
    i = 0
    n = len(T)
    while i < n and pos < 0:
        if T[i] == k:
            pos = i

        i += 1


    return(pos)

def rechercheDicho(T,k):
    n = len(T)
    l = 0
    r = n - 1
    i = int((l+r)/2)
    while (T[i] != k) and (l <= r):
        if k < T[i]:
            r = i - 1
        else:
            l = i + 1

        i = int((l+r)/2)

    if k == T[i]:
        return(i)
    else:
        return(-1)

#Main

print("Génération d'un tableau")
genereTableau(10000)
print("Entrez un élément à trouver")

fin = False
while not(fin):
    k = int(input("Nombre à rechercher"))
    if k == -1:
        fin = True

    else:
        tpø = time.clock()
        ps1 = rechercheSeq(T,k)
        tp1 = time.clock()
        ps2 = rechercheDicho(T,k)
        tp2 = time.clock()


        if ps1 == -1 or ps2 ==-1 :
            print("le nombre n'a pas été trouvé")
        else :
            print("La recherche séquentielle à trouvé le nombre à la position :",ps1)
            print("Durée de la recherche séquentielle : ", tp1-tpø)

            print("La recherche dichotomique à trouvé le nombre à la position :",ps2)
            print("Durée de la recherche dichotomique : ", tp2-tp1)



#choix = int(input())
#ps = rechercheSeq(T,choix)
#if ps < 0:
#    print("Le nombre n'a pas été trouvé")
#else:
#    print("Le nombre a été trouvé à la position :", ps)

