import json
import random
import time
from fonctions_utiles import clearscreen

def salle_du_tresor():
    """
    Simulation de l'épreuve finale : trouver le mot-code pour ouvrir le coffre.
    """
    try:
        # Chargement des données JSON
        with open("data/indicesSalle.json", "r", encoding="utf-8") as f:
            f_dict = json.load(f) # load le dictionnaire principal
    except FileNotFoundError:
        print("Erreur : le fichier indicesSalle.json est introuvable.")
        return False
    except :
        # pour gérer tout autre type d'exception durant l'ouverture et la lecture du fichier
        return False

    f_dict = f_dict["Fort Boyard"] # selectionne le sous dictionnaire de l'émission fort boyard
    if not f_dict:
        print("Erreur : il manque des données dans le fichier indice")
        return

    em_list = list(f_dict.values()) # récupère les émissions (valeurs) indépendamment des années (clées)
    em_rnd = random.choice(em_list)
    em_rnd = list(em_rnd.values())[0]

    indices = em_rnd["Indices"]
    code = em_rnd["MOT-CODE"].strip()

    if len(indices) < 4 or not code:
        print("Erreur : données insuffisantes pour l'épreuve.")
        return

    # Afficher les trois premiers indices
    print("Indices disponibles :", ",".join(indices[:3]))
    found = False

    for i in range(1, 4):
        print("Alors, quel est le mot-code ?")
        reponse = input("=> ").strip()
        if reponse == code:
            print("Bravo, vous avez trouvé le mot-code !")
            return True
        else:
            print(f"Non, ce n'est pas le mot-code. Il vous reste {3 - i} essai(s).")
            time.sleep(1)
            if i < 3:
                print("Voici un autre indice :")
                print(indices[2 + i])
                time.sleep(1)

    if not found:
        print(f"Vous n'avez pas trouvé le mot-code (qui était '{code}').")
        time.sleep(1)
        print("Le coffre reste fermé. VOUS AVEZ PERDU !")
        return False

salle_du_tresor()
