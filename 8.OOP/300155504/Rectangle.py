"""
Fichier : Rectangle.py
Description : Classe Rectangle héritant de Figure
Auteur : 300155504
Date : 2025-12-10
"""

from figure import Figure

class Rectangle(Figure):
    def _init_(self, largeur, hauteur):
        super()._init_("Rectangle")
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def afficher_info(self):
        return f"{super().afficher_info()}, L={self.largeur}, H={self.hauteur}, aire={self.aire()}"