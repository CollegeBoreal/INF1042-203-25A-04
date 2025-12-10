"""
Fichier : prisme_losange.py
Description : Classe prisme losange héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure

class prisme_losange(Figure):
    def __init__(self, d1, d2, hauteur):
        super().__init__("prisme losange")
        self.d1 = float(d1)
        self.d2 = float(d2)
        self.hauteur = float(hauteur)

    def volume(self):
        base = (self.d1 * self.d2) / 2
        return base * self.hauteur

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, d1={self.d1}, d2={self.d2}, "
            f"hauteur={self.hauteur}, volume={self.volume():.2f}"
        )
