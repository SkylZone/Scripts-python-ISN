# Descentes en profondeur et largeur dans un graphe orienté ou non.
# LLA 2018

n = 6   # Nombre de sommets du graphe

matAdj = [[0,1,1,0,0,0],
          [0,0,0,0,1,0],
          [1,0,0,1,0,0],
          [0,1,0,0,0,0],
          [0,0,0,0,0,0],
          [0,1,0,1,1,0]],

aps = [0 for k in range(n)]
fs = []
explore = []


def matAdjTabSuccess(n):
    # Produit les tableaux aps et fs des successeurs à  partir d'une matrice d'adjacence matAdj
    global aps, fs

    k = 0
    for i in range(n):
        aps[i] = k
        for j in range(n):
            if matAdj[i][j] != 0:
                fs.append(j+1)
                k += 1
        fs.append(0)
        k += 1

def gamma(s):
    # Retourne l'ensemble des successeurs du sommet s

    X = []
    i = aps[s-1]
    while fs[i] != 0:
        X.append(fs[i])
        i += 1

    return X

def descenteProfondeur(s):
    Marquee
    rp(s)
    def rp(s):
        var t :sommets

        Marquee[s]=True

            if not Marquee(t)de gamma





    # Algorithme de descente en profondeur à partir du sommet s


# A VOUS D'ECRIRE CETTE PARTIE

def descenteLargeur(s):
    finDescente = False
    k = 0
    x = {s}
    Marquee = (0,0,0,0,0,0)
    while not finDescente:
        k = k+1
        #Marquer tout les sommets de # X
        Y =



    # Algorithme de descente en largeur à partir du sommet s

 # A VOUS D'ECRIRE CETTE PARTIE


#MAIN
print('\n')

matAdjTabSuccess(n)
print(aps,fs)

fin = False
while not(fin):
    s = int(input("Descente à partir du sommet (0 pour quitter) ? "))
    if s == 0:
        fin = True
    else:
        if s < (n+1):

            print("Descente en largeur à partir du sommet ",s," :\n")
            explore = [False for k in range(n)]
            descenteLargeur(s)
            print("Descente en profondeur à partir du sommet ",s," :\n")
            explore = [False for k in range(n)]
            descenteProfondeur(s)

print('\n')
