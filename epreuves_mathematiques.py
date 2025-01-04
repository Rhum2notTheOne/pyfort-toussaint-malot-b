from fonctions_utiles import clearscreen
import time
import random


def factorielle(n):  # Retourne la factorielle de n de manière récursive
    return 1 if n == 0 else n * factorielle(n - 1)


def epreuve_math_factorielle():  # fonction de l'épreuve de factorielle
    print(
        "Bienvenue dans l'épreuve de factorielle ! Ton objectif est de donner le resultat d'une factorielle."
    )
    time.sleep(1)
    print("exemple : la factorielle de 3 est 3! = 3*2*1 = 6")
    time.sleep(1)
    clearscreen()
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


def resoudre_equation_lineaire():  # Génère une équation linéaire sous la forme ax + b = 0 et retourne les valeurs a, b et la solution.
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    solution = -b / a
    return a, b, solution


def epreuve_math_equation():  # Épreuve de résolution d'équation linéaire.
    print(
        "Bienvenue dans l'épreuve de résolution d'équation linéaire ! Ton objectif est de trouver la valeur de x qui résout une équation de la forme ax + b = 0."
    )

    a, b, solution = resoudre_equation_lineaire()
    clearscreen()
    print("Résouds cette équation : ", a, "x + ", b, " = 0")
    reponse = float(input("Quelle est la valeur de x ?\n=> "))
    clearscreen()
    print("Voyons voir...")
    time.sleep(2)
    if reponse == solution:
        print("Bravo, tu as gagné une clé !")
        time.sleep(2)
        return True
    else:
        print("Dommage, mauvaise réponse !")
        time.sleep(2)
        return False


def est_premier(n):  # Vérifie si un nombre est premier.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def premier_plus_proche(n):  # Retourne le premier nombre premier supérieur ou égal à n.
    while not est_premier(n):
        n += 1
    return n


def epreuve_math_premier():  # Épreuve des nombres premiers : le joueur doit trouver le nombre premier le plus proche.
    clearscreen()
    print(
        "Bienvenue dans l'épreuve des nombres premiers ! Ton objectif est de trouver l'entier premier le plus proche de celui qui va t'être donné"
    )
    time.sleep(1)
    print("exemple : le nbr_jr premier le plus proche de 10 est 11")
    time.sleep(1)
    clearscreen()
    n = random.randint(10, 20)
    solution = premier_plus_proche(n)
    print("Trouve le nombre premier le plus proche de", n)
    reponse = int(input("Quel est ce nombre ?\n=> "))
    clearscreen()
    print("Voyons voir...")
    time.sleep(2)
    if reponse == solution:
        print("Bravo, tu as gagné une clé !")
        time.sleep(2)
        return True
    else:
        print("Dommage, mauvaise réponse ! Le bon nombre était", solution)
        time.sleep(2)
        return False


def epreuve_roulette_mathematique():  # Épreuve de la roulette mathématique : addition, soustraction ou multiplication des nombres générés.
    clearscreen()
    print(
        "Bienvenue dans l'épreuve de la roulette mathématique ! Ton objectif est de calculer le résultat d'une opération (addition, soustraction ou multiplication) appliquée à une série de nombres qui te seront donnés."
    )
    time.sleep(1)
    solution = -1
    nombres = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(["+", "-", "*"])
    if operation == "+":
        solution = sum(nombres)
        # utilisation de la fonction prédéfinie sum sur les arrays
    if operation == "-":
        solution = nombres[0]
        for num in nombres[1:]:
            solution -= num
    if operation == "*":
        solution = 1
        for num in nombres:
            solution *= num

    clearscreen()
    print("Voici les nombres sur la roulette :", nombres)
    print("Calcule le résultat en utilisant l'opération :", operation)
    reponse = int(input("Quel est le résultat ?\n=> "))
    clearscreen()
    print("Voyons voir...")
    time.sleep(2)
    if reponse == solution:
        print("Bravo, tu as gagné une clé !")
        time.sleep(2)
        return True
    else:
        print("Dommage, mauvaise réponse ! Le bon résultat était", solution)
        time.sleep(2)
        return False


def pick():  # Sélectionne et exécute aléatoirement une épreuve mathématique.
    clearscreen()

    epreuves = [
        epreuve_math_factorielle,  # Liste des épreuves mathématiques disponibles
        epreuve_math_equation,
        epreuve_math_premier,
        epreuve_roulette_mathematique,
    ]

    epreuve_choisie = random.choice(epreuves)  # Sélection aléatoire d'une épreuve
    return epreuve_choisie()
