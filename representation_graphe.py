n = 6 # Nombre de sommets du graphe

matAdj = [[0,1,0,1],
          [1,0,0,0],
          [1,1,0,0],
          [0,0,0,1]]

def matAdjTabSuccess(n):
    # Produit les tableaux aps et fs des succes

    global aps, fs
    aps = [0,3,5,8]
    fs = [2,4,0,1,0,1,2,0,4,0]
