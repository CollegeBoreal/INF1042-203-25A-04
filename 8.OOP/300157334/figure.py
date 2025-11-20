
"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300157334]
Date : 19-11-2025
"""

class Figure:
    def __init__(self, nom):
      
        self.nom = nom

    def afficher_info(self):
        # Retourne une chaîne contenant le nom de la figure
        return f"Figure: {self.nom}"

    def aire(self):
        # Méthode à implémenter par les sous-classes
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

