liste_nb = [99, 45, 9, 35, 68, 10, 612, 72, 53, 100]
n = 10
print("Première version de la liste")
print(liste_nb)
liste_nb.append(205)
print("Deuxième version de la liste")
print(liste_nb)
print("Liste triée")
liste_nb.sort()
while (n>=0):
	print(liste_nb[n])
	n=n-1
print("Suppression du nombre 53")
liste_nb.remove(53)
print(liste_nb)
print("la longeur de la liste est", len(liste_nb))
