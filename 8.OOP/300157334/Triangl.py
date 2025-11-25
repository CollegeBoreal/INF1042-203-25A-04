"""
Fichier : Triangl.py
Description : Classe Triangl héritant de Figure
Auteur : 300157334
Date : 2025-11-19
"""

from figure import Figure

class Triangl(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangl")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        # Aire d'un triangl : (base * hauteur) / 2
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, "
            f"base={self.base}, hauteur={self.hauteur}, aire={self.aire()}"
        )
