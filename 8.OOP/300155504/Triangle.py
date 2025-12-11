"""
Projet POO — Figures géométriques
Auteur      : BADREDDINE BARRAGOUB
Matricule   : 300155504
Fichier     : Triangle.py
Description : Classe Triangle qui hérite de Figure.
"""

__author__ = "BADREDDINE BARRAGOUB"
__student_id__ = "300155504"

from figure import Figure
import matplotlib.pyplot as plt
from math import sqrt


class Triangle(Figure):
    """Triangle rectangle simple."""

    def __init__(self, base: float, hauteur: float) -> None:
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self) -> float:
        return (self.base * self.hauteur) / 2

    def perimetre(self) -> float:
        """On suppose un triangle rectangle isocèle."""
        hyp = sqrt(self.base**2 + self.hauteur**2)
        return self.base + self.hauteur + hyp

    def dessiner(self, axe: plt.Axes) -> None:
        """Dessine un triangle rectangle : (0,0), (base,0), (0,hauteur)."""
        xs = [0, self.base, 0, 0]
        ys = [0, 0, self.hauteur, 0]
        axe.plot(xs, ys)
        axe.set_aspect("equal")
        marge_x = self.base * 0.2
        marge_y = self.hauteur * 0.2
        axe.set_xlim(-marge_x, self.base + marge_x)
        axe.set_ylim(-marge_y, self.hauteur + marge_y)
        axe.set_title(f"Triangle (base={self.base}, hauteur={self.hauteur})")
