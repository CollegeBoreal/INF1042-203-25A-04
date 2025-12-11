"""
Fichier : Triangle.py
Description : Classe Carré héritant de Figure
Auteur : [300156615]
Date : 2025-12-06
"""
from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire():.2f}"
