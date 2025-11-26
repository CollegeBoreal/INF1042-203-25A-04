
Fichier : trapeze.py
Description : Classe Trapèze héritant de Figure
Auteur : [300151483]
Date : 2025-11-26
"""

from figure import Figure

class Trapeze(Figure):
    def __init__(self, base1, base2, hauteur):
        super().__init__("Trapèze")
        self.base1 = base1
        self.base2 = base2
        self.hauteur = hauteur

    def aire(self):
        # Formule de l'aire d'un trapèze : ((base1 + base2) * hauteur) / 2
        return ((self.base1 + self.base2) * self.hauteur) / 2

    def afficher_info(self):
        return (f"{super().afficher_info()}, base1={self.base1}, "
                f"base2={self.base2}, hauteur={self.hauteur}, aire={self.aire()}")
