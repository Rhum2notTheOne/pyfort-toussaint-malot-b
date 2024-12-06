import os


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
