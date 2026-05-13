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

#Mise en pourcentage de la distance entre la planète et le Soleil par rapport à la distance
# entre l'Aphélie de Pluton et le Soleil
def to_percentage_distance(distance, distance_max) :
    
    return distance * (100/distance_max)

#Mise en pourcentage de la taille de la planète par rapport à la taille du Soleil
def to_percentage_taille(taille_planete, taille_max) :

    return taille_planete * (100/taille_max)

#Mise à l'échelle de la distance trouvée
def a_lechelle_distance(indexe1, indexe2) :
    
    pourcentage = to_percentage_distance(systeme_solaire.CorpsCelesteTest[indexe1][indexe2], systeme_solaire.distance_max)

    return (602 * (pourcentage*(1e-2)))

#Mise à l'échelle de la taille trouvée
def a_lechelle_taille(indexe1_planete, indexe2_planete, indexe1_max, indexe2_max) :
    
    pourcentage = to_percentage_taille(systeme_solaire.CorpsCelesteTest[indexe1_planete][indexe2_planete], systeme_solaire.CorpsCelesteTest[indexe1_max][indexe2_max])

    return pourcentage

#Changement du point d'origine du Canva (haut gauche into milieu)
def to_cartesian(canvas_height, canvas_length, x, y):

    return (canvas_length/2) + x, (canvas_height/2) - y
 
#PLANETES
######################################################################

#Cercle SOLEIL
hauteur = 600
largeur = 600

HG = to_cartesian(hauteur, largeur, -30, -30)
BD = to_cartesian(hauteur, largeur, 30, 30)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='yellow')

#Cercle MERCURE
HG = to_cartesian(hauteur, 670 + int(a_lechelle_distance(1, 1)), int(-a_lechelle_taille(1, 5, 0, 5)), int(-a_lechelle_taille(1, 5, 0, 5)))
BD = to_cartesian(hauteur, 670 + int(a_lechelle_distance(1, 1)), int(a_lechelle_taille(1, 5, 0, 5)), int(a_lechelle_taille(1, 5, 0, 5)))

print("Taille minus :", int(-a_lechelle_taille(1, 5, 0, 5)))
print("Taille plus :", int(a_lechelle_taille(1, 5, 0, 5)))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='grey')

#canvas.create_line((2, 300), (602, 300), width=1, fill='red')

#systeme_solaire.ForceGravitationnelle()


root.mainloop()

iterations = 0

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    print("Soleil - " + name + ": Force gravitationnelle X :", Fx)
    print("-----------------------------")