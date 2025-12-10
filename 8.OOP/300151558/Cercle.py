"""
Fichier : Cercle.py
Description : Classe Cercle héritant de Figure
<<<<<<< HEAD
Auteur : [ID de l'étudiant]
Date : YYYY-MM-DD
"""

from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")  # Appel du constructeur de la classe de base
        self.rayon = rayon           # Rayon du cercle

    def aire(self):
        # Calcul de l'aire du cercle
        return math.pi * self.rayon ** 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, le rayon et l'aire
        return f"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}"
=======
Auteur : 300151558
Date : 2025-11-19
class Carre:
    def _init_(self, cote):
        self.cote = cote

    def aire(self):
        return self.cote * self.cote
>>>>>>> 1fdca5b6a9d167f09d462fb7c0c2b32b0b52c8b7
