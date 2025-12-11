"""
Projet POO — Figures géométriques
Auteur      : BADREDDINE BARRAGOUB
Matricule   : 300155504
Fichier     : Carre.py
Description : Classe Carre qui hérite de Figure.
"""

__author__ = "BADREDDINE BARRAGOUB"
__student_id__ = "300155504"

from Figure import Figure
import matplotlib.pyplot as plt


class Carre(Figure):
    """Représente un carré de côté donné."""

    def __init__(self, cote: float) -> None:
        super().__init__("Carre")
        self.cote = cote

    def aire(self) -> float:
        return self.cote**2

    def perimetre(self) -> float:
        return 4 * self.cote

    def dessiner(self, axe: plt.Axes) -> None:
        """Dessine un carré dont le coin inférieur gauche est à (0,0)."""
        xs = [0, self.cote, self.cote, 0, 0]
        ys = [0, 0, self.cote, self.cote, 0]
        axe.plot(xs, ys)
        axe.set_aspect("equal")
        marge = self.cote * 0.2
        axe.set_xlim(-marge, self.cote + marge)
        axe.set_ylim(-marge, self.cote + marge)
        axe.set_title(f"Carré (côté={self.cote})")

    def afficher_info(self) -> str:
        """Retourne une description textuelle du carré."""
        return (
            f"Carré de côté {self.cote} — "
            f"aire = {self.aire():.2f}, périmètre = {self.perimetre():.2f}"
        )
