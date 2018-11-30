def pgcd(na,nb):
	while (na != nb):
		if na>nb:
			na=na-nb
		else:
			nb=nb-na
	return na

print("Veuillez entrer 2 nombres entiers positifs")
print("Veuillez entrer le premier nombre")
x=int(input())
print("Veuillez entrer le deuxième nombre")
y=int(input())
print("Le plus grand diviseur commun est",pgcd(x,y))