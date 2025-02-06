# 1/Projet Phase 1
# 1:Import des bibliothèques nécessaires
from tkinter import *
import random

#2:Initialisation du fenêtre de jeu avec des dimensions et de titre approprié.
window = Tk()
window.title("Pierre, Papier, Ciseau")
window.geometry("800x600")

#3:Définition de la couleur d'arrière-plan de la fenêtre.
window.configure(bg="#7263d9")

#4:Création d'une étiquette pour le titre du jeu et l'affichée.
label = Label(window, text="Jeu Pierre, Papier, Ciseau", font=("Arial", 25), bg="#7263d9", fg="#edeafa")
label.pack(pady=20)

#5:Invitation de l’utilisateur à choisir entre pierre, papier ou ciseaux.
choix_utilisateur_label = Label(window, text="Choisissez : Pierre, Papier ou Ciseaux", fg="#000000")
choix_utilisateur_label.pack(pady=10)

#:6Création d'un champ de saisie pour que l'utilisateur puisse saisir son choix.
entree_utilisateur = Entry(window)
entree_utilisateur.pack()

#7:Génération d'une sélection aléatoire pour l'ordinateur (pierre, papier ou ciseaux).
def choisir_option_utilisateur():
    choix = entree_utilisateur.get().lower()
    if choix in ["pierre", "papier", "ciseaux"]:
        return choix
    else:
        resultat_label.config(text="Choix invalide. Veuillez réessayer.")
        return None

#8:Affectation la sélection générée aléatoirement à la variable comp_pick.
# Choix de l'ordinateur
def choisir_option_ordinateur():
    options = ["pierre", "papier", "ciseaux"]
    return random.choice(options)

#2/Projet Phage 2
#1:Implémentation les instructions conditionnelles nécessaires pour déterminer le gagnant.
def determiner_gagnant(choix_utilisateur, choix_ordinateur):
    regles = {
        "pierre": "ciseaux",
        "ciseaux": "papier",
        "papier": "pierre"
    }

    if choix_utilisateur == choix_ordinateur:
        return "Égalité !"
    elif regles[choix_utilisateur] == choix_ordinateur:
        return "Vous avez gagné !"
    else:
        return "L'ordinateur a gagné !"

#1:Définition d'une fonction appelée play() pour gérer la logique du jeu.
def play():
    choix_utilisateur = choisir_option_utilisateur()
    if choix_utilisateur:
        choix_ordinateur = choisir_option_ordinateur()
        resultat = determiner_gagnant(choix_utilisateur, choix_ordinateur)
        resultat_label.config(text=f"Vous avez choisi : {choix_utilisateur}\nL'ordinateur a choisi : {choix_ordinateur}\n{resultat}")
        entree_utilisateur.delete(0, END)  # Efface le champ de saisie après le coup

#2:Définition d'une fonction appelée Reset() pour réinitialiser le jeu.
play_bouton = Button(window, text="PLAY", command=play)


#3:Définition d'une fonction appelée Reset() pour réinitialiser le jeu.
reset_bouton = Button(window, text="RESET", command=lambda: resultat_label.config(text=""))  # Réinitialise le label de résultat

#4:Définition d'une fonction appelée Exit() pour quitter l'application
exit_bouton = Button(window, text="EXIT", command=window.destroy)  # Ferme la fenêtre

#3/Projet Phage 3
#1:Créatiion d'un champ de saisie pour afficher le résultat du jeu et Lions-le à la variable Result.
resultat_label = Label(window, text="")
resultat_label.pack(pady=10)

#4:Définition d'un bouton appelé « PLAY » pour lancer le jeu lorsque vous cliquez dessus. Associons-le à la fonction play().
play_bouton.pack(pady=10)

#5:Définissez un bouton appelé « RESET » pour réinitialiser le jeu lorsque vous cliquez dessus. Liez-le à la fonction Reset().
reset_bouton.pack(pady=10)

#6:Définition d'un bouton appelé « EXIT » pour quitter l'application lorsque vous cliquez dessus. Lions-le à la fonction Exit()
exit_bouton.pack(pady=10)

#7:Exécution de l'application en appelant root.mainloop() pour démarrer le jeu Pierre, Papier, Ciseaux.
window.mainloop()