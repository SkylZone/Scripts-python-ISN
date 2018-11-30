print("Veuillez entrer une année à tester")
annee = int(input())
if (annee%4==0) or ((annee%400==0) and (annee%400==0)):
	print("L'année",annee,"est une année bissextile")
else:
	print("L'année",annee,"n'est pas une année bissextile")