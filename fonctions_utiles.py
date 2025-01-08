import os
import time


def introduction():
    """
    Explique les règles du jeu Fort Boyard.
    """
    clearscreen()
    print("=" * 40)
    print(" Bienvenue dans Fort Boyard ! ")
    print("=" * 40)
    print("\nVoici les règles du jeu :")
    print("1. Formez une équipe de 1 à 3 joueurs.")
    print("2. Chaque joueur participera à des épreuves.")
    print("3. Vous pouvez faire 4 types d'épreuves :")
    print("   - Mathématiques : Faites des calculs ")
    print("   - Hasard : Tentez votre chance avec des dés ou jeux aléatoires.")
    print("   - Logique : Réfléchissez et essayez de battre le maître du jeu.")
    print("   - Énigmes : Répondez aux questions du Père Fouras.")
    print("4. Quand vous avez 3 clés, vous pouvez entrer dans la salle du trésor.")
    print("5. Dans la salle, utilisez les indices pour deviner le mot-code.")
    print("\nBut : Trouvez le trésor en gagnant des clés et en devinant le mot-code.")
    print("\nBonne chance !!!")
    print("=" * 40)
    input("\nAppuyez sur Entrée pour continuer...")
    clearscreen()


def composer_equipe():
    """
    Crée une équipe de 1 à 3 joueurs, demande si le joueur est leader,
    et s'assure qu'un leader est désigné.
    """
    equipe = []
    while True:
        clearscreen()
        try:
            nbr_jr = int(
                input(
                    "=> Combien de joueurs voulez-vous dans votre équipe ? (1 à 3) : "
                )
            )
            if 1 <= nbr_jr <= 3:
                break
            print("Le nombre doit être entre 1 et 3.")
        except ValueError:
            print("Entrez un nombre entier valide.")

    leader = False  # Pour vérifier si un leader a été désigné
    leader_found = False
    for i in range(nbr_jr):
        while True:
            print(f"\n| Joueur {i + 1} |")
            nom = input("Nom : ").strip()
            emploi = input("Emploi : ").strip()
            if nom == "" or emploi == "":  # Vérifie si les champs sont vides
                print("Nom ou emploi vide. Veuillez réessayer.")
                continue

            # Demande si le joueur est le leader
            if not leader_found:
                is_leader = (
                    input("Est-ce le leader de l'équipe ? (o/n) : ").strip().lower()
                )
                leader = is_leader == "o"
                if leader:
                    leader_found = True
            equipe.append(
                {"nom": nom, "emploi": emploi, "clees": 0, "leader": leader}
            )
            leader = False
            break

    # Si aucun leader n'a été désigné, on définit le premier joueur comme leader
    if not leader_found:
        print(
            "\nAucun leader n'a été désigné. Le premier joueur sera automatiquement désigné comme leader."
        )
        time.sleep(2)
        equipe[0]["leader"] = True

    # Affiche l'équipe finale
    print("\nVotre équipe :")
    for i, joueur in enumerate(equipe, 1):
        leader_status = "Leader" if joueur["leader"] else "Membre"
        print(
            f"Joueur {i}: {joueur['nom']} ({joueur['emploi']}) - Clés : {joueur['cles_gagnees']} - {leader_status}"
        )
    time.sleep(2)

    return equipe


def choix_joueur(equipe):
    """Permet au leader de l'équipe de choisir un joueur pour l'épreuve"""
    while True:
        clearscreen()
        print("\nChoisissez le joueur qui participera à l'épreuve :")
        for i, joueur in enumerate(equipe, 1):
            print(f"{i} - {joueur['nom']} ({joueur['emploi']})")
        try:
            choix = int(input("=> "))
            if choix < 1 or choix > len(equipe):
                raise ValueError
            return equipe[choix - 1]
        except ValueError:
            print(f"Veuillez entrer un nombre entre 1 et {len(equipe)}")


def clearscreen():
    """
    efface l'ecran suivant l'os
    """
    # Vérifie si on est sous Windows
    if os.name == "nt":
        os.system("cls")
    # Pour les autres systèmes
    else:
        os.system("clear")


def choix_epreuves():
    """
    Permet au joueur de choisir une épreuve parmi les différentes catégories.
    Retourne le nom de l'épreuve sélectionnée (sous forme de chaîne).
    """
    epreuves = [
        "epreuves_hasard",
        "epreuves_logique",
        "epreuves_mathematiques",
        "enigme_pere_fouras",
    ]

    while True:
        clearscreen()
        print("Choisissez une épreuve parmi les suivantes :")
        for i, ep in enumerate(epreuves, start=1):
            print(f"{i}. {ep}")
        try:
            choice = int(input("=> "))
            if 1 <= choice <= len(epreuves):
                return epreuves[choice - 1]
            else:
                print(f"Veuillez entrer un nombre entre 1 et {len(epreuves)}.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
