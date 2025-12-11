"""
Fichier : Parallelogramme.py
Description : Classe Parallélogramme héritant de Figure
Auteur : [300155045]
Date : 2025-12-06
"""

from figure import Figure

class Parallelogramme(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Parallélogramme")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return self.base * self.hauteur

    def afficher_info(self):
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire():.2f}"

