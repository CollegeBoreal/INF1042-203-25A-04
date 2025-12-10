"""
Fichier : Carre.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300151449]
Date : 2025-11-26
"""

from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")  # Appel du constructeur de la classe de base
        self.cote = cote           # Longueur du côté du carré

    def aire(self):
        # Calcul de l'aire du carré
        return self.cote ** 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, le côté et l'aire
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"
