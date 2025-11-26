class Parallelogramme:
    def _init_(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return self.base * self.hauteur

    def afficher_info(self):
        return (
            f"Parallélogramme - Base : {self.base}, "
            f"Hauteur : {self.hauteur}, Aire : {self.aire()}"
        )