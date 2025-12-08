"""
Fichier : hexagone.py
Description : Classe Hexagone régulier
Auteur : 300155109
Date : 2025-12-07
"""

import math
from figure import Figure

class Hexagone(Figure):
    def __init__(self, cote):
        if cote <= 0:
            raise ValueError("Le côté doit être positif.")
        self.cote = cote

    def aire(self):
        # Aire d'un hexagone régulier : (3 * sqrt(3) / 2) * côté^2
        return (3 * math.sqrt(3) / 2) * (self.cote ** 2)

    def afficher_info(self):
        return (
            f"Figure : Hexagone, côté={self.cote}, "
            f"aire={self.aire():.2f}"
        )
