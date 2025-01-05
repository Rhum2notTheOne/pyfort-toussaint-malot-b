import json
import random
from fonctions_utiles import clearscreen
import time

def charger_enigmes(fichier):
    """
    Charge les énigmes depuis un fichier JSON.
    """
    with open(fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)
    return enigmes

def enigme_pere_fouras():
    """
    Le joueur doit résoudre une énigme en 3 essais.
    """
    enigmes = charger_enigmes("data/enigmesPF.json")
    enigme_choisie = random.choice(enigmes)
    question = enigme_choisie["question"]
    reponse_attendue = enigme_choisie["reponse"].lower()
    essais = 3

    print("")
    clearscreen()
    print("Voici l'énigme du Père Fouras :")
    print(question)

    while essais > 0:
        reponse = input("Quelle est votre réponse ?\n=> ").strip().lower()
        clearscreen()
        if reponse == reponse_attendue:
            print("Bravo ! Bonne réponse, vous gagnez une clé !")
            time.sleep(2)
            return True
        else:
            essais -= 1
            if essais > 0:
                print("Mauvaise réponse. Il vous reste", essais, "essai(s).")
            else:
                print("Vous avez perdu. La bonne réponse était :", reponse_attendue)
                time.sleep(2)
                return False
