from figure import Figure
from math import pi

class Cercle(Figure):
    """
    Classe représentant un cercle.
    """

    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return pi * self.rayon ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, rayon = {self.rayon}, aire = {self.aire():.2f}"

