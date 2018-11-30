from tkinter import *
from random import randrange

def drawLine():

    palette=['red','yellow','green','blue','purple','aqua','orange','silver']
    c = randrange(0,8)
    couleur = palette[c]
    x1 = randrange(side)
    y1 = randrange(side)
    x2 = randrange(side)
    y2 = randrange(side)
    can1.create_line(x1,y1,x2,y2,width = 2,fill = couleur)


def clearCanevas():
    can1.delete(ALL)


#Main

side = 400

fen1 = Tk()
can1 = Canvas(fen1,bg='grey',height=side,width=side)
can1.pack(side=LEFT)

boutton2 = Button(fen1, text = 'Tracer', command = drawLine)
boutton2.pack(side = LEFT, padx = 5, pady = 5)

boutton1 = Button(fen1, text = 'Quitter', command = fen1.quit)
boutton1.pack(side = LEFT, padx = 5, pady = 5)

#Démarrage de l'observateur d'évènement
fen1.mainloop()
#Déstruction en sortie du programme
