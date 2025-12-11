# Signature : BadrEddine Barragoub - 300155504

"""
Fichier : Cercle.py
Description : Classe Cercle héritant de Figure.
Auteur : 300155504
Date : 2025-12-10
"""

from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def afficher_info(self):
        return f"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}"

