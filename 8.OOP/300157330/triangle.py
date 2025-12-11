"""
Fichier : Triangle.py
Description : Classe représentant un triangle simple (base et hauteur).
Auteur : [300157330]
Date : 2025-11-25
"""

class Triangle:
    """
    Classe représentant un triangle défini par une base et une hauteur.
    """

    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        """
        Calcule l'aire du triangle.
        """
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        """
        Retourne une chaîne contenant les informations du triangle.
        """
        return f"Triangle : base = {self.base}, hauteur = {self.hauteur}, aire = {self.aire()}"
