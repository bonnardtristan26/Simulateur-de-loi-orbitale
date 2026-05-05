import tkinter as tk

 
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
canvas = tk.Canvas(root, width=600, height=400, bg='black')

canvas.pack(anchor=tk.CENTER, expand=True)
######################################################################

#CERCLE

hauteur = 400
largeur = 600

HG = to_cartesian(400, 600, -50, -50)
BD = to_cartesian(400, 600, 50, 50)


points =(
    HG,
    BD
)

canvas.create_oval(*points, fill='yellow')

# Lancement de la boucle principale

root.mainloop()
 
#AFFICHAGE D'UN TEXTE
######################################################################
#label_instruction = tk.Label(root, text="Entrez votre nom :")

#label_instruction.pack(pady=10)
######################################################################
 
#ZONE D'ENTREE DE TEXTE
######################################################################
#entree = tk.Entry(root)

#entree.pack()
######################################################################

#BOUTON
######################################################################
#bouton = tk.Button(root, text="exemple", command=exemple-fonction)

#bouton.pack(pady=10)
######################################################################
 

for i in range(iterations):
    print("Iteration", i + 1)
    print("-----------------------------")
    print("Soleil - " + name + ": Force gravitationnelle X :", Fx)
    print("-----------------------------")