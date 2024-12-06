import random
import time
from fonctions_utiles import clearscreen


def bonneteau():
    """
    fonction de l'épreuve du bonneteau
    """
    clearscreen()
    print("Bienvenue au jeu de bonneteau !")
    print(
        "Dans ce jeu, vous devez retrouver la bille cachée sous l'un des trois gobelets."
    )
    time.sleep(3)
    tentatives = 0
    liste_gobelets = ["a", "b", "c"]
    while tentatives < 2:
        clearscreen()
        tentatives += 1
        choix = -1
        print("Attention, je mélange les gobelets...")
        time.sleep(2)
        while choix not in liste_gobelets:
            clearscreen()
            choix = input("Choisissez un gobelet (a, b ou c) : \n=>").lower()
        time.sleep(2)
        pick = random.randint(0, 2)
        if choix == liste_gobelets[pick]:
            print("Bravo, vous avez gagné la clée !")
            time.sleep(2)
            return True
        elif tentatives == 1:
            print("Perdu ! Mais je vous laisse une seconde chance.")
        else:
            print("Perdu ! La bille était sous le gobelet", liste_gobelets[pick])
            time.sleep(2)
            return False
        time.sleep(3)


def jeu_lance_des():
    """
    fonction de l'épreuve du jeu de lancer de dés
    """
    clearscreen()
    print("Bienvenue au jeu du lancé de dés !")
    print("Dans ce jeu, vous devez être le premier à obtenir un 6 en lançant un dé.")
    time.sleep(4)
    tentatives = 0
    while tentatives < 3:
        clearscreen()
        tentatives += 1
        input("Allons y, appuie sur entrée pour lancer les dés !")
        print("...")
        time.sleep(1)
        picks = [random.randint(1, 6), random.randint(1, 6)]
        print(str(picks[0]), "|", str(picks[1]))
        time.sleep(2)
        if picks[0] == 6 or picks[1] == 6:
            print("Oh, vous avez gagné la clé !")
            time.sleep(2)
            return True
        clearscreen()
        print("Pas de chance...")
        time.sleep(2)
        print("Au tour du maitre du jeu de lancer les dés !")
        time.sleep(2)
        print("...")
        time.sleep(1)
        picks = [random.randint(1, 6), random.randint(1, 6)]
        print(str(picks[0]), "|", str(picks[1]))
        time.sleep(2)
        if picks[0] == 6 or picks[1] == 6:
            print("Bien joué maitre du jeu, vous méritez votre place...")
            time.sleep(2)
            return False
        print("Vous aussi ?!")
        time.sleep(2)


def pick():
    fonctions_epreuves = [bonneteau, jeu_lance_des]
    return random.choice(fonctions_epreuves)()
