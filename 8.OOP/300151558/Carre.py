"""
Fichier : Carre.py
Description : Classe Carré héritant de Figure
Auteur : [ID de l'étudiant]
Date : YYYY-MM-DD
"""
class Carre:
    def _init_(self, cote):
        self.cote = cote

    def aire(self):
        return self.cote * self.cote
