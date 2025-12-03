"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré, un cercle et un triangle
             puis affiche leurs informations.
Auteur : [300155606]
Date : 2025-11-26
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle   # <-- nouvelle figure ajoutée

def main():
    """
    Fonction principale : créer plusieurs figures géométriques
    et afficher leurs informations via le polymorphisme.
    """

    # Création des figures
    carre = Carre(4)           # Carré de côté 4
    cercle = Cercle(3)         # Cercle de rayon 3
    triangle = Triangle(5, 2)  # Triangle base=5 et hauteur=2

    # Liste polymorphique
    figures = [carre, cercle, triangle]

    # Affichage automatique selon le type de figure
    for f in figures:
        print(f.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()
