# Signature : BadrEddine Barragoub - 300155504

"""
Fichier : Figure.py
Description : Classe de base représentant une figure géométrique.
Auteur : 300155504
Date : 2025-12-10
"""

class Figure:
    def __init__(self, nom):
        self.nom = nom

    def aire(self):
        """Méthode à redéfinir dans les classes enfants."""
        raise NotImplementedError("La méthode aire() doit être définie dans la sous-classe.")

    def afficher_info(self):
        """Retourne les infos de base de la figure."""
        return f"Figure : {self.nom}"


