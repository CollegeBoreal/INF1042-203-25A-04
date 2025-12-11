"""
Fichier : prisme_parallelogramme.py
Description : Classe prisme parallelogramme héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure

class prisme_parallelogramme(Figure):
    def __init__(self, base, hauteur_parallelo, profondeur):
        super().__init__("prisme parallelogramme")
        self.base = float(base)
        self.hauteur_parallelo = float(hauteur_parallelo)
        self.profondeur = float(profondeur)

    def volume(self):
        return self.base * self.hauteur_parallelo * self.profondeur

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, base={self.base}, "
            f"hauteur={self.hauteur_parallelo}, profondeur={self.profondeur}, "
            f"volume={self.volume():.2f}"
        )
