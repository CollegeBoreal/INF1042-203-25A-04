"""
Fichier : carre.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300158185]
Date : 1998-08-10
"""

from figure import Figure

class carre(Figure):
    def __init__(self, cote):
        super().__init__("carre")  # Appel du constructeur de la classe de base
        self.cote = cote           # Longueur du côté du carre

    def aire(self):
        # Calcul de l'aire du carre
        return self.cote ** 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, le côté et l'aire
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"
