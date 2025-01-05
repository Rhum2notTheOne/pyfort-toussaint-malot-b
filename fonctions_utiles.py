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
    time.sleep(2)
    clearscreen()


def composer_equipe():
    """
    Crée une équipe de 1 à 3 joueurs, demande si le joueur est leader,
    et s'assure qu'un leader est désigné.
    """
    equipe = []
    while True:
        try:
            nbr_jr = int(input("=> Combien de joueurs voulez-vous dans votre équipe ? (1 à 3) : "))
            if 1 <= nbr_jr <= 3:
                break
            print("Le nombre doit être entre 1 et 3.")
        except ValueError:
            print("Entrez un nombre entier valide.")

    leader = False  # Pour vérifier si un leader a été désigné
    leader_found = False
    for i in range(nbr_jr):
        print(f"\n| Joueur {i + 1} |")
        nom = input("Nom : ").strip()
        emploi = input("Emploi : ").strip()

        # Demande si le joueur est le leader
        if not leader_found:
            is_leader = input("Est-ce le leader de l'équipe ? (o/n) : ").strip().lower()
            leader = is_leader == "o"
            if leader:
                leader_found = True
        equipe.append({"nom": nom, "emploi": emploi, "cles_gagnees": 0, "leader": leader})
        leader = False

    # Si aucun leader n'a été désigné, on définit le premier joueur comme leader
    if not leader_found:
        print("\nAucun leader n'a été désigné. Le premier joueur sera automatiquement désigné comme leader.")
        equipe[0]["leader"] = True

    # Affiche l'équipe finale
    print("\nVotre équipe :")
    for i, joueur in enumerate(equipe, 1):
        leader_status = "Leader" if joueur["leader"] else "Membre"
        print(f"Joueur {i}: {joueur['nom']} ({joueur['emploi']}) - Clés : {joueur['cles_gagnees']} - {leader_status}")

    return equipe


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


def presentation(epreuve):
    clearscreen()
    if epreuve == "bataille_navale":
        print("Bienvenue dans le jeu de la bataille navale!")
        time.sleep(1)
        print(
            "Le terrain de jeu est de taille 3x3, et ton objectif est de couler tous les bateaux ennemis !"
        )
    if epreuve == "factorielle":
        print(
            "Bienvenue dans l'épreuve de factorielle ! Ton objectif est de donner le resultat d'une factorielle"
        )
        time.sleep(1)
        print("exemple : la factorielle de 3 est 3! = 3*2*1 = 6")
    if epreuve == "premier":
        print(
            "Bienvenue dans l'épreuve de nbr_jr premier ! Ton objectif est de trouver l'entier premier le plus proche de celui qui va t'être donné"
        )
        time.sleep(1)
        print("exemple : le nbr_jr premier le plus proche de 10 est 11")
