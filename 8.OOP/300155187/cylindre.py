"""
Fichier : cylindre.py
Description : Classe cylindre héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure
import math

class cylindre(Figure):
    def __init__(self, rayon, hauteur):
        super().__init__("cylindre")  # Appel du constructeur de la classe de base
        self.rayon = float(rayon)     # Rayon du cylindre
        self.hauteur = float(hauteur) # Hauteur du cylindre

    def volume(self):
        # Calcul du volume du cylindre : π r² h
        return math.pi * self.rayon**2 * self.hauteur

    def afficher_info(self):
        # Retourne une chaîne contenant le rayon, la hauteur et le volume
        return (
            f"{super().afficher_info()}, "
            f"rayon={self.rayon}, hauteur={self.hauteur}, volume={self.volume():.2f}"
        )