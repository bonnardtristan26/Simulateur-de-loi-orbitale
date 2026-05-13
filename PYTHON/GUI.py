import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath("C:/Users/Administrateur/Documents/GitHub/Simulateur-de-loi-orbitale/système_solaire"))

import systeme_solaire

# Création de la fenêtre principale
######################################################################
root = tk.Tk()

root.title("Ma Super App")

root.geometry("1400x700")
######################################################################

#CREATION DE LA FENETRE DE DESSIN
######################################################################
canvas = tk.Canvas(root, width=600, height=600, bg='black')

canvas.pack(anchor=tk.CENTER, expand=True)
######################################################################

#FONCTIONS
######################################################################

def to_percentage(distance, distance_max) :
    
    return distance * (100/distance_max)

def a_lechelle(indexe1, indexe2) :
    
    pourcentage = to_percentage(systeme_solaire.CorpsCelesteTest[indexe1][indexe2], systeme_solaire.distance_max)
    
    print("A l'échelle :", 600 * (pourcentage*(1e-2)))
    
    return 600 * (pourcentage*(1e-2))
    
    #et faudra faire de même pour la taille de la planète
 
def to_cartesian(canvas_height, canvas_length, x, y):

    return (canvas_length/2) + x, (canvas_height/2) - y
 
 

#CERCLE SOLEIL

hauteur = 600
largeur = 600

HG = to_cartesian(hauteur, largeur, -30, -30)
BD = to_cartesian(hauteur, largeur, 30, 30)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='yellow')

#CERCLE MERCURE

HG = to_cartesian(hauteur, a_lechelle(1, 1), -10, -10)
BD = to_cartesian(hauteur, a_lechelle(1, 1), 10, 10)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='grey')

#systeme_solaire.ForceGravitationnelle()


root.mainloop()

iterations = 0

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    print("Soleil - " + name + ": Force gravitationnelle X :", Fx)
    print("-----------------------------")