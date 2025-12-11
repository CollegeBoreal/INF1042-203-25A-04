"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300155086]
Date : 2003-07-03
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
        return (f"{super().afficher_info()}, largeur={self.largeur}, "
                f"hauteur={self.hauteur}, aire={self.aire():.2f}")
