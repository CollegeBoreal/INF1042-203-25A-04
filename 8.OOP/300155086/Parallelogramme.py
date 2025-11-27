"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300155086]
Date : 2003-07-03
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
        return (f"{super().afficher_info()}, base={self.base}, "
                f"hauteur={self.hauteur}, aire={self.aire():.2f}")
