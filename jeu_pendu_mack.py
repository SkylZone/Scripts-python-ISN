from random import *
liste = ["alkekenge", "arbouse", "bigarade", "carambole", "chataigne", "cornouiller", "combava",
"cynorrhodon", "grenade", "jujube", "kumquat", "mangoustan", "myrobolan", "noisette", "myrtille", "nefle",
"pasteque", "physalis", "pistache", "quetsche"]

def choisir_mot():
    mot_choisi=choice(list)
    return mot_choisi

def in_lettre():
    lettre = input("Entrer une letrre")
    lettre = lettre.lower()
    return lettre

def masque(mot_complet, lettres):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres:
            mot_masque = mot_masque+lettre
        else:
            mot_masque = mot_masque + "-"
    return mot_masque

recom=True
while recom:
    nb_essai = 10
    print("Jeu du pendu")
    print("Son but est de trouver un mot")
    print("caché en moins de 10 essais")
    mot_inconnu = choisir_mot()
    lettres_ok = []
    mot = masque(mot_inconnu, lettre_ok)
    while mot_inconnu!=mot and nb_essai>0:
        print("Mot à trouver", mot, "-> Il vous reste", nb_essai, "coup(s)")