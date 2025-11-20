"""
Fichier : Carre.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300155086]
Date : 2003-07-03
"""
from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"
