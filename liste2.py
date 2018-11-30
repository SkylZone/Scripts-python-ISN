from random import *
print("liste aléatoire de 10 éléments réels")
liste_reel= [0]*10
for i in range(10):
	liste_reel[i]=random()
	print(liste_reel[i])
print("\nsérie aléatoire de 10 éléments entiers")
for i in range(10):
	print(randrange(3, 18, 3), end ='') 