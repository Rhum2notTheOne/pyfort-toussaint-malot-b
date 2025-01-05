import epreuves_hasard
import epreuves_logique
import epreuves_mathematiques
import enigme_pere_fouras
import epreuve_finale
import random
from fonctions_utiles import clearscreen


def main():
    clees = 0
    epreuves = {
        "epreuves_hasard": epreuves_hasard,
        "epreuves_logique": epreuves_logique,
        "epreuves_mathematiques": epreuves_mathematiques,
        "epreuve_finale": epreuve_finale,
    }
    while clees < 3:
        clearscreen()
        print("Choisissez une épreuve parmi les suivantes :")
        for i, ep in enumerate(epreuves.keys()):
            # choix le plus lisible, vu que epreuves.keys() est un dict_keys et non une liste
            # on est obligé d'itérer de cette manière pour avoir les indices en plus
            print(i + 1, "|", ep)
        try:
            choice = int(input("=>"))
            if choice < 1 or choice > len(epreuves.keys()):
                raise ValueError
            ep = list(epreuves.values())[choice - 1]
            if ep.pick():
                clees += 1
            # un choix en dehors des limites va être considéré comme une ValueError
        except TypeError or ValueError:
            print(f"Veuillez entrer un nombre entre 1 et {len(epreuves.keys())}")
            continue


if __name__ == "__main__":
    main()
