from fonctions_utiles import clearscreen
import time
import random


def factorielle(n):
    """
    Retourne la factorielle de n de manière récursive
    """
    return 1 if n == 0 else n * factorielle(n - 1)


def epreuve_math_factorielle():
    """
    fonction de l'épreuve de factorielle
    """
    print("")
    pick = random.randint(1, 10)
    clearscreen()
    if int(input(f"Calcule donc la factorielle de {pick} !\n=>")) == factorielle(pick):
        time.sleep(1)
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

epreuve_math_factorielle()


def resoudre_equation_lineaire():
    """
    fonction de la résolution d'équation linéaire
    """
    a,b = random.randint(1, 10)
    solution = -b/a

def epreuve_math_equation():
