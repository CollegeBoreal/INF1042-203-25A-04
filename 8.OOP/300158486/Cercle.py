"""
Fichier : Cercle.py
Description : Classe Cercle héritant de Figure
Auteur : 300158486
Date : 2025-11-25
"""

from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}"
