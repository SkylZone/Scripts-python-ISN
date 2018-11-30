from random import *
print("liste aléatoire de 10 éléments réels")
liste_reel=[0]*10
for i in range(10):
	liste_reel[i]=randint(0,10)

liste_reel.sort()
print(liste_reel)
print("le nombre le plus petit est", min(liste_reel))
print("le nombre le plus grand est", max(liste_reel))
print("Suprression du nombre le plus petit et du nombre le plus grand")
liste_reel.remove(min(liste_reel))
liste_reel.remove(max(liste_reel))
print(liste_reel)
