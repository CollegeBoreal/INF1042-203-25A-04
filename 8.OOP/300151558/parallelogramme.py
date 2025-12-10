"""
Fichier : Parallelogramme.py
Description : Classe Carré héritant de Figure
Auteur : [hindchili]
Date : 2025.12.10
"""

from figure import Figure

class Parallelogramme(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Parallélogramme")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return self.base * self.hauteur

    def afficher_info(self):
        return (
            f"Parallélogramme - Base : {self.base}, "
            f"Hauteur : {self.hauteur}, Aire : {self.aire()}"
        )

    
