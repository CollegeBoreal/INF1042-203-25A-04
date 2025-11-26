"""
Fichier : losange.py
Description : Classe losange héritant de Figure
Auteur : [300155187]
Date : 2005-11-25
"""

from figure import Figure

class losange(Figure):
    def __init__(self, d1,d2):
        super().__init__("losange")  # Appel du constructeur de la classe de base
        self.d1 = float(d1) # Longueur du grand D du losange
        self.d2 = float(d2) # Longueur du petit d du losange
                              

    def aire(self):
        # Calcul de l'aire du losange
        return (self.d1 * self.d2) / 2

    def afficher_info(self):
        # Retourne une chaîne contenant le grand D, le petit d et l'aire
        return f"{super().afficher_info()}, d1={self.d1}, d2={self.d2}, aire={self.aire()}"