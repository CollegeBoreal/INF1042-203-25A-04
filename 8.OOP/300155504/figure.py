"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques
Auteur : 300155504
Date : 2025-12-03
"""

class Figure:
    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        return f"Figure: {self.nom}"

    def aire(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

