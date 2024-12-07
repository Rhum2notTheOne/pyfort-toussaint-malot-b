from fonctions_utiles import clearscreen
import time
import random


def factorielle(n):
    """
    Retourne la factorielle de n de manière récursive
    """
    return 1 if n == 0 else n * factorielle(n - 1)


def epreuve_factorielle():
    """
    fonction de l'épreuve de factorielle
    """
    print("")
    pick = random.randint(0, 10)
    clearscreen()
    if int(input(f"Calcule donc la factorielle de {pick} !\n=>")) == factorielle(pick):
        time.sleep(2)
        clearscreen()
        print("Voyons voir...")
        time.sleep(2)
        print("Bravo, tu as gagné une clée !")
        time.sleep(2)
        return True
    else:
        time.sleep(2)
        clearscreen()
        print("Voyons voir...")
        time.sleep(2)
        print("Dommage, tu as perdu !")
        time.sleep(2)
        return False


epreuve_factorielle()
