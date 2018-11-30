from random import *
inconnu = randint(1,101)
ch=cpt=0
print ("Trouver le plus vite possible un nombre entre 1 et 100")
while inconnu != ch:
	ch=int(input("Entrer votre nombre"))
	if ch>inconnu:
		print("C'est trop grand")
	else:
		print("C'est trop petit")
	cpt=cpt+1
print("Bravo vous avez trouvé en",cpt,"coup(s)")
