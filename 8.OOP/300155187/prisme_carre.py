"""
Fichier : prisme_carre.py
Description : Classe prisme carré héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure

class prisme_carre(Figure):
    def __init__(self, cote, hauteur):
        super().__init__("prisme carré")
        self.cote = float(cote)
        self.hauteur = float(hauteur)

    def volume(self):
        return self.cote**2 * self.hauteur

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, "
            f"cote={self.cote}, hauteur={self.hauteur}, volume={self.volume():.2f}"
        )