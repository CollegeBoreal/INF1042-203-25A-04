# Signature : BadrEddine Barragoub - 300155504
"""
Fichier : Losange.py
Description : Classe Losange héritant de Figure.
Auteur : 300155504
Date : 2025-12-10
"""

from figure import Figure

class Losange(Figure):
    def _init_(self, d1, d2):
        super()._init_("Losange")
        self.d1 = d1
        self.d2 = d2

    def aire(self):
        return (self.d1 * self.d2) / 2

    def afficher_info(self):
        return (
            f"{super().afficher_info()}, "
            f"d1={self.d1}, d2={self.d2}, aire={self.aire()}"
        )