"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [300152315]
Date : 2025-11-19
"""

from Carre import Carre
from Cercle import Cercle

def main():
    """
    Fonction principale du programme.
    Crée un carré et un cercle, puis affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    # Affichage des informations des deux figures
    print(c1.afficher_info())
    print(c2.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()