"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré, un cercle et un triangle, puis affiche leurs informations.
Auteur : [300157330]
Date : 2025-11-25
"""

from Carre import Carre
from Cercle import Cercle
from triangle import Triangle  # <<< Nouveau import

def main():
    """
    Fonction principale du programme.
    Crée un carré, un cercle et un triangle, puis affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    # Création d'un triangle (base 5, hauteur 6)
    t1 = Triangle(5, 6)

    # Affichage des informations
    print(c1.afficher_info())
    print(c2.afficher_info())
    print(t1.afficher_info())  # <<< Nouveau affichage

# Point d'entrée du programme
if __name__ == "__main__":
    main()
