from random import*
inconnu = randint(1,101)

def test(a,b):
		if (a>b):
			print("Le nombre est trop petit")
		elif (a<b):
			print("Le nombre est trop grand")
		elif (a == b):
			print("Vous avez trouvé, le nombre était", a)

print("Un nombre aléatoire entre 1 et 100 a été généré")
print("Faites un choix")
c = int(input())
while (c != inconnu):
	c = int(input())
	test(inconnu,c)






