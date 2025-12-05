from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur

    def afficher_info(self):
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire()}"
