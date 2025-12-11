# Signature : BadrEddine Barragoub - 300155504
"""
Fichier : Etoile.py
Description : Classe Etoile héritant de Figure.
Auteur : 300155504
Date : 2025-12-11
"""

from figure import Figure


class Etoile(Figure):
    def _init_(self, taille: float):
        # on appelle le constructeur de la classe mère Figure
        super()._init_("Étoile")
        self.taille = taille

    def aire(self) -> float:
        """
        Aire symbolique pour une étoile (ce n'est pas une vraie formule géométrique).
        Ici on prend simplement taille * taille * 2.
        """
        return self.taille * self.taille * 2

    def afficher_info(self) -> str:
        """Retourne une description complète de l'étoile."""
        return f"{super().afficher_info()}, taille={self.taille}, aire={self.aire()}"