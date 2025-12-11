"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300151483]
Date : 2011-11-11
"""

# figure.py
class Figure:
    def __init__(self, nom):
        self.nom = nom

    def aire(self):
        raise NotImplementedError("La méthode aire() doit être définie dans les sous-classes")

    def afficher_info(self):
        return f"Figure: {self.nom}"
