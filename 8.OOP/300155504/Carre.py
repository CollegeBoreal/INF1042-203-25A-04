"""
Fichier : Carre.py
Description : Classe Carré héritant de Figure
Auteur : 300155504
Date : 2025-12-11
"""

from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"
