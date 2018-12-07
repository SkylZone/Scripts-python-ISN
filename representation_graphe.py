n = 6 # Nombre de sommets du graphe

matAdj = [[0,1,0,1],
          [1,0,0,0],
          [1,1,0,0],
          [0,0,0,1]]

def matAdjTabSuccess(n):
    # Produit les tableaux aps et fs des succes

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
