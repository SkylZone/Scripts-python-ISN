
def hanoi(n, t1, t2, t3):
    global s
    if n > 0:
        hanoi(n-1, t1, t3, t2)
        print(t1, "-->", t3)
        hanoi(n-1, t2, t1, t3)
        s += 1

#main

print("Jeu de hanoi \nObjectif : déplacer tous les disques du socle A sur le socle C.  ")

s = 0
n = input("Donner le nombre de disques sur le socle A :")
n=int(n)

print("Le protocole est le suivant")
print("")

hanoi(n, 'A', 'B', 'C')
print("Nombre d'étapes : ", s)

