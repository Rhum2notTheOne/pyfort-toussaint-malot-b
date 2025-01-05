import json
import random
import time
from fonctions_utiles import clearscreen


def charger_enigmes(fichier):
    """
    Charge les énigmes depuis un fichier JSON.
    """
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            enigmes = json.load(f)
        if not isinstance(enigmes, list):
            raise ValueError("Le fichier JSON doit contenir une liste d'énigmes.")
        return enigmes
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Erreur lors du chargement des énigmes : {e}")
        return []


def enigme_pere_fouras():
    """
    Pose une énigme au joueur, qui a 3 essais pour donner la bonne réponse.
    """
    enigmes = charger_enigmes("data/enigmesPF.json")
    if not enigmes:
        print("Impossible de jouer : aucune énigme disponible.")
        time.sleep(2)
        return

    # Sélection d'une énigme aléatoire
    enigme_choisie = random.choice(enigmes)
    question = enigme_choisie.get("question", "Pas de question disponible.")
    reponse_attendue = enigme_choisie.get("reponse", "").strip().lower()

    if not question or not reponse_attendue:
        print("L'énigme choisie est mal formatée.")
        time.sleep(2)
        return

    # Affichage de l'énigme et gestion des essais
    essais = 3
    clearscreen()
    print("Voici l'énigme du Père Fouras :")
    print(question)

    while essais > 0:
        reponse = input("Quelle est ta réponse ?\n=> ").strip().lower()
        clearscreen()
        if reponse == reponse_attendue:
            print("Bravo ! Bonne réponse, tu gagnes une clé !")
            time.sleep(2)
            return True
        else:
            essais -= 1
            if essais > 0:
                print(f"Mauvaise réponse. Il te reste {essais} essai(s).")
            else:
                print("Tu as perdu. La bonne réponse était :", reponse_attendue)
                time.sleep(2)
                return False


def pick():
    return enigme_pere_fouras()
