n = 6 # Nombre de sommets du graphe

matAdj = [[0,1,1,0,0,0],
          [0,0,0,0,1,0],
          [1,0,0,1,0,0],
          [0,1,0,0,0,0],
          [0,0,0,0,0,0],
          [0,1,0,1,1,0]]

def matAdjTabSuccess(n):
    # Produit les tableaux aps et fs des succes

    global aps, fs
