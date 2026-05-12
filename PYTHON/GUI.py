import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath("C:/Users/tristan.bonnard.STFL/Documents/GitHub/Simulateur-de-loi-orbitale/système_solaire"))

import systeme_solaire

# Création de la fenêtre principale
######################################################################
root = tk.Tk()

root.title("Ma Super App")

root.geometry("1000x700")
######################################################################

#CREATION DE LA FENETRE DE DESSIN
######################################################################
canvas = tk.Canvas(root, width=800, height=400, bg='black')

canvas.pack(anchor=tk.CENTER, expand=True)
######################################################################

#FONCTIONS
######################################################################
#def a_lechelle(planete_height, planet_lenght) :
    
    #DISTANCE MAXIMALE DE CANVA
    #planète la plus éloignée + marge de pixels pour pas que ça dépasse le canva = distance maximale
    
    #par rapport a cette distance max, il faudra remettre à l'échelle les distances des planètes pour que ça reste réaliste
    #mais que ça reste visible dans le canva
    
    #et faudra faire de même pour la taille de la planète
 
def to_cartesian(canvas_height, canvas_length, x, y):

    return (canvas_length/2) + x, (canvas_height/2) - y
 
 

#CERCLE SOLEIL

hauteur = 400
largeur = 800

HG = to_cartesian(hauteur, largeur, -50, -50)
BD = to_cartesian(hauteur, largeur, 50, 50)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='yellow')

#CERCLE MERCURE

HG = to_cartesian(hauteur, 1200, -20, -20)
BD = to_cartesian(hauteur, 1200, 20, 20)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='red')

#systeme_solaire.ForceGravitationnelle()


root.mainloop()

iterations = 1000

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    print("Soleil - " + name + ": Force gravitationnelle X :", Fx)
    print("-----------------------------")