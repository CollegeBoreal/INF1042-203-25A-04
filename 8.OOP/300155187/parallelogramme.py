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
        self.b = float(b) # Longueur du grand D du losange
        self.h = float(h) # Longueur du petit d du losange
                              

    def aire(self):
        # Calcul de l'aire du losange
        return (self.b * self.h)

    def afficher_info(self):
        # Retourne une chaîne contenant le grand D, le petit d et l'aire
        return f"{super().afficher_info()}, b={self.b}, h={self.h}, aire={self.aire()}"