"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300155086]
Date : 2003-07-03
"""
import math
from figure import Figure

class Hexagone(Figure):
    def __init__(self, cote):
        super().__init__("Hexagone régulier")
        self.cote = cote

    def aire(self):
        return (3 * math.sqrt(3) / 2) * (self.cote ** 2)

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire():.2f}"
