import epreuve_finale
import epreuves_hasard
import epreuves_logique
import enigme_pere_fouras
import epreuves_mathematiques
from fonctions_utiles import (
    introduction,
    clearscreen,
    composer_equipe,
    choix_joueur,
    choix_epreuves,
)


def jeu():
    epreuves = {
        "epreuves_hasard": epreuves_hasard,
        "epreuves_logique": epreuves_logique,
        "epreuves_mathematiques": epreuves_mathematiques,
        "enigme_pere_fouras": enigme_pere_fouras,
    }
    introduction()
    clees = 0
    participants = composer_equipe()
    while clees < 3:
        clearscreen()
        ep = epreuves[choix_epreuves()]
        participant = choix_joueur(participants)
        if ep.pick():
            # cette écriture est permise par le polymorphisme ;
            # si ep.pick retourne vrai alors
            # c'est que le joueur à réussi l'epreuve choisie
            participant["clees"] += 1
            clees += 1
    epreuve_finale.salle_du_tresor()
    # epreuve finale, le moment ou l'on doit deviner le mot clé


if __name__ == "__main__":
    jeu()
