class Terrain:
    def __init__(self, n=3) -> None:
        self.grille = [["0" for _ in range(n)] for _ in range(n)]
        self.bateaux_coules = 0

    def ajouter_bateau(self, x: int, y: int) -> None:
        self.grille[x][y] = "B"

    def touche(self, x: int, y: int) -> bool:
        """
        fonction à utiliser pour déterminer si une attaque touche un de vos bateaux
        """
        if self.grille[x][y] == "B":
            return True
        return False

    def __str__(self) -> str:
        """
        print(Terrain) affiche la grille du terrain de manière propre
        """
        return "\n".join(["|".join([str(col) for col in line]) for line in self.grille])
