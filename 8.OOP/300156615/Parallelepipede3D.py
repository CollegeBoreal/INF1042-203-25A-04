"""
Fichier : Parallelepipede3D.py
Description : Classe Parallélépipède 3D (volume et sommets)
Auteur : [300156615]
Date : 2025-12-11
"""

import numpy as np


class Parallelepipede3D:
    def __init__(self, origine, v1, v2, v3):
        """
        origine : point de départ (x, y, z)
        v1, v2, v3 : vecteurs formant les arêtes 3D
        """
        self.O = np.array(origine, dtype=float)
        self.v1 = np.array(v1, dtype=float)
        self.v2 = np.array(v2, dtype=float)
        self.v3 = np.array(v3, dtype=float)

    def volume(self):
        """Volume = produit mixte |v1 · (v2 × v3)|"""
        return abs(np.dot(self.v1, np.cross(self.v2, self.v3)))

    def sommets(self):
        """Retourne les 8 sommets du parallélépipède"""
        O = self.O
        v1 = self.v1
        v2 = self.v2
        v3 = self.v3

        return np.array([
            O,
            O + v1,
            O + v2,
            O + v1 + v2,
            O + v3,
            O + v1 + v3,
            O + v2 + v3,
            O + v1 + v2 + v3
        ])

