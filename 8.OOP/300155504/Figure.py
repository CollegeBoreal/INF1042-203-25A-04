"""
Projet POO — Figures géométriques
Auteur      : BADREDDINE BARRAGOUB
Matricule   : 300155504
Fichier     : figure.py
Description : Classe de base pour les figures géométriques.
"""

__author__ = "BADREDDINE BARRAGOUB"
__student_id__ = "300155504"


class Figure:
    """Classe de base pour toutes les figures géométriques."""

    def __init__(self, nom: str) -> None:
        self.nom = nom

    def aire(self) -> float:
        """Retourne l'aire de la figure (méthode abstraite)."""
        raise NotImplementedError("La méthode aire() doit être redéfinie dans la sous-classe.")

    def perimetre(self) -> float:
        """Retourne le périmètre de la figure (méthode abstraite)."""
        raise NotImplementedError("La méthode perimetre() doit être redéfinie dans la sous-classe.")

    def dessiner(self, axe):
        """Dessine la figure sur l'axe donné (méthode abstraite)."""
        raise NotImplementedError("La méthode dessiner() doit être redéfinie dans la sous-classe.")
