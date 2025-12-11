"""
Fichier : cone.py
Description : Classe cône héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure
import math

class cone(Figure):
    def __init__(self, rayon, hauteur):
        super().__init__("cone")
        self.rayon = float(rayon)
        self.hauteur = float(hauteur)

    def volume(self):
        return (1/3) * math.pi * self.rayon**2 * self.hauteur

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, rayon={self.rayon}, "
            f"hauteur={self.hauteur}, volume={self.volume():.2f}"
        )