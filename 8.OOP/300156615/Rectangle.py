"""
Fichier : Rectangle.py
Description : Classe Carré héritant de Figure
Auteur : [300156615]
Date : 2025-12-06
"""
from figure import Figure

class Rectangle(Figure):
    def __init__(self, largeur, hauteur):
        super().__init__("Rectangle")
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, largeur={self.largeur}, "
            f"hauteur={self.hauteur}, aire={self.aire():.2f}"
        )
