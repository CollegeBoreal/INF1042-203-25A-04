"""
Projet POO — Figures géométriques
Auteur      : BADREDDINE BARRAGOUB
Matricule   : 300155504
Fichier     : Triangle.py
Description : Classe Triangle qui hérite de Figure.
"""

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
        hyp = sqrt(self.base**2 + self.hauteur**2)
        return self.base + self.hauteur + hyp

    def dessiner(self, axe: plt.Axes) -> None:
        xs = [0, self.base, 0, 0]
        ys = [0, 0, self.hauteur, 0]
        axe.plot(xs, ys)
        axe.set_aspect("equal")
        marge = 0.2
        axe.set_xlim(-1, self.base + 1)
        axe.set_ylim(-1, self.hauteur + 1)
        axe.set_title(f"Triangle (base={self.base}, hauteur={self.hauteur})")

    def afficher_info(self) -> str:
        return (
            f"Triangle (base={self.base}, hauteur={self.hauteur}) — "
            f"aire = {self.aire():.2f}, périmètre = {self.perimetre():.2f}"
        )
