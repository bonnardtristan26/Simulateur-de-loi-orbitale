import tkinter as tk
 
def saluer():

    nom = entree.get()

    label_message.config(text=f"Bonjour {nom} !")
 
# Création de la fenêtre principale

root = tk.Tk()

root.title("Ma Super App")

root.geometry("300x200")
 
# Ajout des composants (Widgets)

label_instruction = tk.Label(root, text="Entrez votre nom :")

label_instruction.pack(pady=10)
 
entree = tk.Entry(root)

entree.pack()
 
bouton = tk.Button(root, text="Valider", command=saluer)

bouton.pack(pady=10)
 
label_message = tk.Label(root, text="")

label_message.pack()
 
# Lancement de la boucle principale

root.mainloop()
 