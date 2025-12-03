"""
Fichier : Carre.py
Description : Classe Carré héritant de Figure
Auteur : 300151558
Date : 2025-11-19
"""
class Carre:
    def _init_(self, cote):
        self.cote = cote

    def aire(self):
        return self.cote * self.cote
