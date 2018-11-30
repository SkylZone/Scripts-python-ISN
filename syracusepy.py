print("Entrez un nombre entier supérieur à 1")
n = int(input())
e = 0
maxi = 0
liste = []
n2 = n

while n>1:
    if n%2 == 0:
        n = n/2
        e += 1
        liste.append(n)
    else:
        n = 3*n +1
        e +=1
        liste.append(n)

maxi = max(liste)
print("Altitude initiale =", int(n2))
print("Durée du vol =", int(e))
print("Altitude maximum =", int(maxi))
