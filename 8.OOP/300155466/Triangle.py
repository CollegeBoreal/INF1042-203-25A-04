"""
Fichier : Triangle.py
Description : Classe Triangle héritant de Figure
Auteur : 30015566
Date : 2001.06.01
"""

from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        # Aire d'un triangle : (base * hauteur) / 2
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, "
            f"base={self.base}, hauteur={self.hauteur}, aire={self.aire()}"
        )
