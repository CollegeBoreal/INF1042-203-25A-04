"""
Fichier : Trapeze.py
Description : Classe Trapèze héritant de Figure
Auteur : 300155109
Date : 2025-12-07
"""

from figure import Figure

class Trapeze(Figure):
    def __init__(self, base1, base2, hauteur):
        super().__init__("Trapèze")
        self.base1 = base1
        self.base2 = base2
        self.hauteur = hauteur

    def aire(self):
        # Formule du trapèze : ((base1 + base2) * hauteur) / 2
        return (self.base1 + self.base2) * self.hauteur / 2

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, "
            f"base1={self.base1}, base2={self.base2}, hauteur={self.hauteur}, "
            f"aire={self.aire()}"
        )

