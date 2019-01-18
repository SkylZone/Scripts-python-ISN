from random import randrange
import time
T = []


def genereTableau(n):
    for i in range (n):
        T.append(randrange(0,1000))
    return(T)

def TriInsertion(T):
    n = len(T)
    for i in range(1,n):
        x = T[i]
        j = i
        while (j>0) and (T[j-1]>x):
            T[j] = T[j-1]
            j = j-1
        T[j] = x

def triBulles(T):
    n = len(T)
    termine = False
    while not(termine):
        for i in range(0,n-1):
            if(T[i+1]<T[i]):
                x = T[i]
                T[i] = T[i+1]
                T[i+1] = x
                termine = False


#main
taille = int(input("Taille du tableau ?"))
T1 = genereTableau(taille)
print(T1)
T2 = T1[:]
tp1 = time.clock()
TriInsertion(T1)
tp2 = time.clock()
triBulles(T2)
tp3 = time.clock()
print(T1,T2)
