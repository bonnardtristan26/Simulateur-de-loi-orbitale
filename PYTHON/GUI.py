import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath("C:/Users/Administrateur/Documents/GitHub/Simulateur-de-loi-orbitale/système_solaire"))

import systeme_solaire

#CREATION DE LA FENETRE DE DESSIN
######################################################################
root = tk.Tk()

root.title("Ma Super App")

root.geometry("1400x700")
######################################################################

#CREATION DE LA FENETRE DE DESSIN
######################################################################
canvas = tk.Canvas(root, width=1300, height=600, bg='black')

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
largeur = 1300

#REPRESENTATION REALISTE
#HG = to_cartesian(hauteur, 1300 + int(a_lechelle_distance(0, 1)), int(-a_lechelle_taille(0, 5, 0, 5)) - 5, int(-a_lechelle_taille(0, 5, 0, 5)) - 5)
#BD = to_cartesian(hauteur, 1300 + int(a_lechelle_distance(0, 1)), int(a_lechelle_taille(0, 5, 0, 5)) + 5, int(a_lechelle_taille(0, 5, 0, 5)) + 5)

#REPRESENTATION NON REALISTE
HG = to_cartesian(hauteur, largeur, -25, -25)
BD = to_cartesian(hauteur, largeur, 25, 25)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='yellow')

################################################################################################################################################""""
#Cercle MERCURE

#REPRESENTATION REALISTE
#Mercure est invisible car sa valeur entière est ~0.3, ce qui est arrondi à 0 par Python.
#Les planètes ayant une valeur de taille au dessus de 5 dixième sont arrondis à l'entier supérieur, quand à ceux en dessous sont arrondis à l'entier inférieur
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(1, 1)), int(-a_lechelle_taille(1, 5, 0, 5)), int(-a_lechelle_taille(1, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(1, 1)), int(a_lechelle_taille(1, 5, 0, 5)), int(a_lechelle_taille(1, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, largeur + 100, -3, -3)
#BD = to_cartesian(hauteur, largeur + 100, 3, 3)

print("Taille minus MERCURE :", -a_lechelle_taille(1, 5, 0, 5))
print("Taille plus MERCURE :", a_lechelle_taille(1, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='grey')

################################################################################################################################################""""
#Cercle VENUS

#REPRESENTATION REALISTE
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(2, 1)), int(-a_lechelle_taille(2, 5, 0, 5)), int(-a_lechelle_taille(2, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(2, 1)), int(a_lechelle_taille(2, 5, 0, 5)), int(a_lechelle_taille(2, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, 150 + largeur, -7, -7)
#BD = to_cartesian(hauteur, 150 + largeur, 7, 7)

print("Taille minus VENUS :", -a_lechelle_taille(2, 5, 0, 5))
print("Taille plus VENUS :", a_lechelle_taille(2, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='tan1')

################################################################################################################################################""""
#Cercle TERRE

#REPRESENTATION REALISTE
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(3, 1)), int(-a_lechelle_taille(3, 5, 0, 5)), int(-a_lechelle_taille(3, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(3, 1)), int(a_lechelle_taille(3, 5, 0, 5)), int(a_lechelle_taille(3, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, 200 + largeur, -7, -7)
#BD = to_cartesian(hauteur, 200 + largeur, 7, 7)

print("Taille minus TERRE :", -a_lechelle_taille(3, 5, 0, 5))
print("Taille plus TERRE :", a_lechelle_taille(3, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='blue3')

################################################################################################################################################""""
#Cercle MARS

#REPRESENTATION REALISTE
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(4, 1)), int(-a_lechelle_taille(4, 5, 0, 5)), int(-a_lechelle_taille(4, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(4, 1)), int(a_lechelle_taille(4, 5, 0, 5)), int(a_lechelle_taille(4, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, 250 + largeur, -4, -4)
#BD = to_cartesian(hauteur, 250 + largeur, 4, 4)

print("Taille minus MARS :", -a_lechelle_taille(4, 5, 0, 5))
print("Taille plus MARS :", a_lechelle_taille(4, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='red3')

################################################################################################################################################""""
#Cercle JUPITER

#REPRESENTATION REALISTE
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(5, 1)), int(-a_lechelle_taille(5, 5, 0, 5)), int(-a_lechelle_taille(5, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(5, 1)), int(a_lechelle_taille(5, 5, 0, 5)), int(a_lechelle_taille(5, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, 365 + largeur, -40, -40)
#BD = to_cartesian(hauteur, 365 + largeur, 40, 40)

#print("Taille minus :", -a_lechelle_taille(5, 5, 0, 5))
#print("Taille plus :", a_lechelle_taille(5, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='burlywood1')

################################################################################################################################################""""
#Cercle SATURNE

#REPRESENTATION REALISTE
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(6, 1)), int(-a_lechelle_taille(6, 5, 0, 5)), int(-a_lechelle_taille(6, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(6, 1)), int(a_lechelle_taille(6, 5, 0, 5)), int(a_lechelle_taille(6, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, 545 + largeur, -35, -35)
#BD = to_cartesian(hauteur, 545 + largeur, 35, 35)

#print("Taille minus :", -a_lechelle_taille(6, 5, 0, 5))
#print("Taille plus :", a_lechelle_taille(6, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='bisque1')

################################################################################################################################################""""
#Cercle URANUS

#REPRESENTATION REALISTE
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(7, 1)), int(-a_lechelle_taille(7, 5, 0, 5)), int(-a_lechelle_taille(7, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(7, 1)), int(a_lechelle_taille(7, 5, 0, 5)), int(a_lechelle_taille(7, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, 670 + largeur, -13, -13)
#BD = to_cartesian(hauteur, 670 + largeur, 13, 13)

#print("Taille minus :", -a_lechelle_taille(7, 5, 0, 5))
#print("Taille plus :", a_lechelle_taille(7, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='snow1')

################################################################################################################################################""""
#Cercle NEPTUNE

#REPRESENTATION REALISTE
HG = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(8, 1)), int(-a_lechelle_taille(8, 5, 0, 5)), int(-a_lechelle_taille(8, 5, 0, 5)))
BD = to_cartesian(hauteur, 1360 + int(a_lechelle_distance(8, 1)), int(a_lechelle_taille(8, 5, 0, 5)), int(a_lechelle_taille(8, 5, 0, 5)))

#REPRESENTATION NON REALISTE
#HG = to_cartesian(hauteur, 745 + largeur, -13, -13)
#BD = to_cartesian(hauteur, 745 + largeur, 13, 13)

#print("Taille minus :", -a_lechelle_taille(8, 5, 0, 5))
#print("Taille plus :", a_lechelle_taille(8, 5, 0, 5))

points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='deepskyblue')

################################################################################################################################################""""

#Creation d'une ligne pour estimer la largeur du canva

#canvas.create_line((2, 300), (1302, 300), width=1, fill='red')

root.mainloop()

iterations = 0

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    print("Soleil - " + name + ": Force gravitationnelle X :", Fx)
    print("-----------------------------")