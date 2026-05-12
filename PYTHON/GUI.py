import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath("C:/Users/tristan.bonnard.STFL/Documents/GitHub/Simulateur-de-loi-orbitale/système_solaire"))

import systeme_solaire
 
def to_cartesian(canvas_height, canvas_length, x, y):

    return (canvas_length/2) + x, (canvas_height/2) - y
 
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

#CERCLE SOLEIL

hauteur = 400
largeur = 600

HG = to_cartesian(400, 600, -50, -50)
BD = to_cartesian(400, 600, 50, 50)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='yellow')

#CERCLE MERCURE

#systeme_solaire.ForceGravitationnelle()


root.mainloop()

iterations = 1000

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    print("Soleil - " + name + ": Force gravitationnelle X :", Fx)
    print("-----------------------------")