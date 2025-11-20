"""
Fichier : Triangle.py
Description : Classe Triangle héritant de Figure
Auteur : [300157334]
Date : 19/11/2025
"""

from figure import Figure

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")  # Appel du constructeur de la classe de base
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        # Calcul de l'aire du triangle
        return 0.5 * self.base * self.hauteur

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, la base, la hauteur et l'aire
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire()}"

