import time
import random
from fonctions_utiles import clearscreen


def print_grid(grid):
    """
    convertit une grille/array 2D en une belle chaîne de caractères
    """
    output = []
    for i, row in enumerate(grid):
        output.append(chr(97 + i) + " " + "|" + "|".join(row))
    output.append("   " + " ".join([str(i) for i in range(1, len(grid) + 1)]))
    return "|\n".join(output)


class Flotte:
    def __init__(self, n, n_b):
        self.grid = [[" " for _ in range(n)] for _ in range(n)]
        self.grid_plan = [[" " for _ in range(n)] for _ in range(n)]
        self.n_b = n_b

    def ajouter_bateau(self, x: int, y: int) -> bool:
        if self.grid[x][y] == "$":
            return False
        self.grid[x][y] = "$"
        return True

    def tir(self, x: int, y: int, flotte) -> bool:
        """
        tire sur la flotte ennemie
        """
        if self.grid_plan[x][y] != " ":
            print("Mais... tu as déjà tiré ici :(")
            time.sleep(2)

        if flotte.grid[x][y] == "$":
            flotte.grid[x][y] = "X"
            flotte.n_b -= 1
            self.grid_plan[x][y] = "X"
            return True
        else:
            self.grid_plan[x][y] = "."
            return False

    def __str__(self):
        """
        print(Flotte)
        affiche le terrain du joueur de manière propre, avec les bateaux
        """
        return print_grid(self.grid)

    def plan(self):
        """
        Flotte.plan()
        affiche le plan d'attaque de manière propre
        """
        return print_grid(self.grid_plan)

    def generer_coos_random(self):
        """
        génère des coordonnées aléatoires non encore utilisées
        """
        while True:
            x = random.randint(0, len(self.grid) - 1)
            y = random.randint(0, len(self.grid) - 1)
            if self.grid_plan[x][y] == " ":
                return x, y


def preparation_flottes():
    clearscreen()
    print("Commencons par préparer ton armée...")
    time.sleep(1)

    x, y = -1, -1
    for i in range(n_b):
        while True:
            clearscreen()
            print(f"Donne moi les coordonnées de ton bateau n°{i+1} !")
            print("-" * 20)
            print(flotte)
            try:
                coos = input("Coordonnées (sous la forme a1): \n=>").lower()
                x = ord(coos.rstrip()[0]) - 97
                y = int(coos.rstrip()[1]) - 1

                if x not in range(n) or y not in range(n):
                    raise ValueError

                if not flotte.ajouter_bateau(x, y):
                    print("Un bateau est déjà présent à cette position (coos) !")
                else:
                    break
            except:
                print(
                    "Tu dois entrer des coordonnées valides (sous la forme a1, b3, ... en restant dans le tableau)"
                )
            time.sleep(2)

    print("ta flotte est fin prête !")
    time.sleep(2)
    clearscreen()
    print("Le maitre du jeu se prépare...")
    for _ in range(n_b):
        while True:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            if flotte_ennemie.ajouter_bateau(x, y):
                break
    time.sleep(2)
    print("Il est prêt !")
    clearscreen()


def attaque():
    while True:
        print("C'est à toi de jouer !")
        clearscreen()
        print("[flotte]")
        print(flotte)
        print("-" * 20)
        print("[plan d'attaque]")
        print(flotte.plan())
        print("-" * 20)
        try:
            coos = input("Coordonnées d'attaque (sous la forme a1): \n=>").lower()
            x = ord(coos.rstrip()[0]) - 97
            y = int(coos.rstrip()[1]) - 1

            if x not in range(n) or y not in range(n):
                raise ValueError

            if not flotte.tir(x, y, flotte_ennemie):
                print("...")
                time.sleep(random.randint(1, 3))
                print("Raté !")
            else:
                print("...")
                time.sleep(random.randint(1, 3))
                print("Touché !")

            time.sleep(2)
            clearscreen()
            break
        except:
            print(
                "Tu dois entrer des coordonnées valides (sous la forme a1, b3, ... en restant dans le tableau)"
            )
            time.sleep(2)


def attaque_ennemie():
    clearscreen()
    print("C'est au tour de l'ennemi...")
    time.sleep(2)
    x, y = flotte_ennemie.generer_coos_random()
    succes = flotte_ennemie.tir(x, y, flotte)
    clearscreen()
    print(f"Le maitre du jeu tire en {chr(x + 97)}{y + 1}")
    if succes:
        print("...")
        time.sleep(random.randint(1, 3))
        print("Et il a touché un de tes bateaux !")
    else:
        print("...")
        time.sleep(random.randint(1, 3))
        print("Il a raté son tir !")
    time.sleep(2)


def bataille_navale():
    clearscreen()
    global n
    global n_b

    n = 3  # taille du terrain
    n_b = 2  # nombre de bateaux

    assert n_b <= n, "Trop de bateaux pour le terrain !"

    print("Bienvenue dans le jeu de la bataille navale!")
    time.sleep(1)
    print(
        "Le terrain de jeu est de taille 3x3, et ton objectif est de couler tous les bateaux ennemis !"
    )
    time.sleep(3)

    global flotte
    global flotte_ennemie

    flotte = Flotte(n, n_b)
    flotte_ennemie = Flotte(n, n_b)

    preparation_flottes()

    while True:
        attaque()
        if flotte_ennemie.n_b == 0:
            print("Mince ! ! ! Tu as coulé tous les bateaux ennemis ! Voici ta clée...")
            return True
        attaque_ennemie()
        if flotte.n_b == 0:
            print(
                "Tu n'as pas réussi à couler tous les bateaux ennemis... Pas de clée pour toi !"
            )
            return False


def pick():
    choices = [bataille_navale]
    return random.choice(choices)()
