"""
Projet POO — Figures géométriques
Auteur      : BADREDDINE BARRAGOUB
Matricule   : 300155504
Fichier     : Cercle.py
Description : Classe Cercle qui hérite de Figure.
"""

__author__ = "BADREDDINE BARRAGOUB"
__student_id__ = "300155504"

from figure import Figure
import matplotlib.pyplot as plt
from math import pi


class Cercle(Figure):
    """Représente un cercle de rayon donné."""

    def __init__(self, rayon: float) -> None:
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self) -> float:
        return pi * self.rayon**2

    def perimetre(self) -> float:
        return 2 * pi * self.rayon

    def dessiner(self, axe: plt.Axes) -> None:
        """Dessine un cercle centré en (0,0)."""
        cercle = plt.Circle((0, 0), self.rayon, fill=False)
        axe.add_patch(cercle)
        axe.set_aspect("equal")
        marge = self.rayon * 0.2
        axe.set_xlim(-self.rayon - marge, self.rayon + marge)
        axe.set_ylim(-self.rayon - marge, self.rayon + marge)
        axe.set_title(f"Cercle (rayon={self.rayon})")
