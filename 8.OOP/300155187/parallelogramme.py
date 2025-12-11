"""
Fichier : parallelogramme.py
Description : Classe  parallelogramme héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure

class  parallelogramme(Figure):
    def __init__(self, b,h):
        super().__init__("parallelogramme")  # Appel du constructeur de la classe de base
        self.b = float(b) # base du parallelogramme
        self.h = float(h) # hauteur du parallelogramme
                              

    def aire(self):
        # Calcul de l'aire du parallelogramme
        return (self.b * self.h)

    def afficher_info(self):
        # Retourne une chaîne contenant la base, l'hauteur et l'aire du parallelogramme
        return f"{super().afficher_info()}, b={self.b}, h={self.h}, aire={self.aire()}"