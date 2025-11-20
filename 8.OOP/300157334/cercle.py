"""
Fichier : Cercle.py
Description : Classe Cercle héritant de Figure
Auteur : 300157334
Date : 19-11-2025
"""

from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        # Aire d'un cercle : π * rayon^2
        return math.pi * (self.rayon ** 2)

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, "
            f"rayon={self.rayon}, aire={self.aire():.2f}"
        )
