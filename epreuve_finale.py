import json
import random
import time
from fonctions_utiles import clearscreen


def salle_Du_Tresor():
    with open("data/indicesSalle.json") as f:
        f_dict = json.load(f)
    f_dict = f_dict["Fort Boyard"]
    em_list = f_dict.values()
    em_rnd = random.choice(em_list)

    indices = em_rnd["Indices"]
    code = em_rnd["MOT-CODE"]

    print(indices[:3])
    found = False
    for i in range(1, 4):
        print("Alors, quel est le mot-code ?")
        if input("=>") == code:
            print("Bravo, vous avez trouvé le mot-code !")
            found = True
            break
        print(f"Non, il ne s'agit pas du mot-code. Il vous reste {3-i} essais.")
        time.sleep(1)
        print("Voici un autre indice :")
        time.sleep(1)
        print(indices[2 + i])
    if not found:
        print(
            f"Vous n'avez pas trouvé le mot-code (qui était {code}). Vous ne pourrez pas ouvrir le coffre."
        )
        print("Vous avez perdu.")
