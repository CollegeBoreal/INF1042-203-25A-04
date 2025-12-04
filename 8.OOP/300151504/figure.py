"""
Fichier : figure.py
Description : Classe de base pour les figures géométriques
Auteur : 300151504
Date : 2025-12-03
"""

class Figure:
    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        return f"Figure : {self.nom}"

    def aire(self):
        raise NotImplementedError("Doit être implémentée dans les sous-classes.")
