from figure import Figure

class Trapeze(Figure):
    def __init__(self, base1, base2, hauteur):   # <-- corriger ici
        super().__init__("Trapeze")
        self.base1 = base1
        self.base2 = base2
        self.hauteur = hauteur

    def aire(self):
        return ((self.base1 + self.base2) * self.hauteur) / 2

    def afficher_info(self):
        return (f"{super().afficher_info()}, base1={self.base1}, "
                f"base2={self.base2}, hauteur={self.hauteur}, aire={self.aire()}")
