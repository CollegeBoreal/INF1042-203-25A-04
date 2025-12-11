from math import pi
from figure import Figure

class Carre(Figure):
    """
    Classe représentant un carré.
    """

    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté = {self.cote}, aire = {self.aire()}"

