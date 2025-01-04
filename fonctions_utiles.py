import os
import time


def clearscreen():
    """
    efface l'ecran suivant l'os
    """
    # Vérifie si on est sous Windows
    if os.name == "nt":
        os.system("cls")
    # Pour les autres systèmes
    else:
        os.system("clear")

def presentation(epreuve):
    clearscreen()
    if epreuve == "bataille_navale": 
        print("Bienvenue dans le jeu de la bataille navale!")
        time.sleep(1)
        print(
            "Le terrain de jeu est de taille 3x3, et ton objectif est de couler tous les bateaux ennemis !"
        )
    if epreuve == "factorielle":
        print("Bienvenue dans l'épreuve de factorielle ! Ton objectif est de donner le resultat d'une factorielle")
        time.sleep(1)
        print("exemple : la factorielle de 3 est 3! = 3*2*1 = 6")
    if epreuve == "premier":
        print("Bienvenue dans l'épreuve de nombre premier ! Ton objectif est de trouver l'entier premier le plus proche de celui qui va t'être donné")
        time.sleep(1)
        print("exemple : le nombre premier le plus proche de 10 est 11")
    if epreuve = ""

