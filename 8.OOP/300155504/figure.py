# Signature : BadrEddine Barragoub - 300155504
"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques.
Auteur : 300155504
Date : 2025-12-10
"""

class Figure:
    def _init_(self, nom):
        # Nom de la figure (ex: Carré, Cercle)
        self.nom = nom

    def afficher_info(self):
        """
        Retourne une chaîne contenant le nom de la figure
        Exemple : "Figure : Carré"
        """
        return f"Figure : {self.nom}"

    def aire(self):
        """
        Méthode à implémenter dans les sous-classes
        """
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")