"""
Fichier : Cylindre.py
Description : Classe Cylindre héritant de Figure.
Auteur : [300157334]
Date : 2025-11-19
"""

from figure import Figure
import math

class Cylindre(Figure):
    """
    Classe représentant un cylindre.
    Hérite de la classe Figure.
    """

    def __init__(self, rayon, hauteur):
        super().__init__("Cylindre")   # Appel au constructeur de Figure
        self.rayon = rayon             # Rayon du cylindre
        self.hauteur = hauteur         # Hauteur du cylindre

    def volume(self):
        """Calcule et retourne le volume du cylindre."""
        return math.pi * self.rayon**2 * self.hauteur

    def aire(self):
        """Calcule et retourne la surface totale du cylindre."""
        return 2 * math.pi * self.rayon * (self.rayon + self.hauteur)

    def afficher_info(self):
        """Retourne les informations du cylindre sous forme de chaîne."""
        return (
            f"{super().afficher_info()}, "
            f"rayon={self.rayon}, "
            f"hauteur={self.hauteur}, "
            f"volume={self.volume():.2f}, "
            f"aire={

