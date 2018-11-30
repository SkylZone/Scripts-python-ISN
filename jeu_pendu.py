from random import *
liste_fruit = ["alkekenge", "arbouse", "bigarade", "carambole", "chataigne", "cornouiller", "combava",
"cynorrhodon", "grenade", "jujube", "kumquat", "mangoustan", "myrobolan", "noisette", "myrtille", "nefle",
"pasteque", "physalis", "pistache", "quetsche"]
n = randint(0,19)
print(liste_fruit[n])
print("Nombre de caractère dans le mot choisit :")
print(len(liste_fruit[n]))
choix_ordi = list(liste_fruit[n])
progression = choix_ordi
c=10

def etoile():
    i = 0
    while i< len(choix_ordi):
        progression[i] = '*'
        i += 1
    return



while c != 0 or progression.count('*') != 0:
    g=str(input("Proposez une lettre"))
    if c==0:
        print("Vous avez perdu")

    elif g in choix_ordi:
        print("Cette lettre est dans le mot")
        print("Coups restants :", c)
        etoile()

    elif g not in choix_ordi:
        print("Cette lettre n'est pas dans le mot")
        c=c-1
        print("Coups restants :", c)
        etoile()












