class Triangle:
    def _init_(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return f"Triangle - Base : {self.base}, Hauteur : {self.hauteur}, Aire : {self.aire()}"