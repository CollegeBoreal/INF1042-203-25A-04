"""
Fichier : Etoile.py
Description : Classe Etoile héritant de Figure
Auteur : 300158486
Date : 2025-11-25
"""

from figure import Figure

class Etoile(Figure):
    def __init__(self, taille):
        super().__init__("Étoile")
        self.taille = taille

    def aire(self):
        # Aire symbolique pour un exemple d'étoile (pas une vraie formule géométrique)
        return self.taille * self.taille * 2

    def afficher_info(self):
        return f"{super().afficher_info()}, taille={self.taille}, aire={self.aire()}"
