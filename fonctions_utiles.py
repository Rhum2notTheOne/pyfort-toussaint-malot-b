import os
import time


def composer_equipe():
    nbr_jr = -1
    while True:
        try:
            nbr_jr = int(
                input("=> Combien de joueurs voulez-vous dans votre équipe ? (1 à 3)")
            )
            if nbr_jr < 1 or nbr_jr > 3:
                break
            else:
                print("Veuillez entrer un nbr_jr entre 1 et 3 !")
        except TypeError:
            print("Veuillez entrer un nbr_jr entier !")
    for i in range(nbr_jr):
        nom = input(f"|Joueur {i+1}| Quel est ton nom ? : ")
        emploi = input(f"|Joueur {i+1}| Quel est ton emploi ? : ")


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
        print(
            "Bienvenue dans l'épreuve de factorielle ! Ton objectif est de donner le resultat d'une factorielle"
        )
        time.sleep(1)
        print("exemple : la factorielle de 3 est 3! = 3*2*1 = 6")
    if epreuve == "premier":
        print(
            "Bienvenue dans l'épreuve de nbr_jr premier ! Ton objectif est de trouver l'entier premier le plus proche de celui qui va t'être donné"
        )
        time.sleep(1)
        print("exemple : le nbr_jr premier le plus proche de 10 est 11")
