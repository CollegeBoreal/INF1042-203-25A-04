"""
Fichier : sphere.py
Description : Classe sphere héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure
import math

class sphere(Figure):
    def __init__(self, rayon):
        super().__init__("sphere")
        self.rayon = float(rayon)

    def volume(self):
        return (4/3) * math.pi * self.rayon**3

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, rayon={self.rayon}, "
            f"volume={self.volume():.2f}"
        )