"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré, un cercle et un cylindre, puis affiche leurs informations.
Auteur : [300157334]
Date : 2025-11-19
"""

from Carre import Carre
from Cercle import Cercle
from Cylindre import Cylindre

def main():
    """
    Fonction principale du programme.
    Crée un carré, un cercle et un cylindre, puis affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    # Création d'un cylindre de rayon 2 et hauteur 5
    c3 = Cylindre(2, 5)

    # Affichage des informations
    print(c1.afficher_info())
    print()
    print(c2.afficher_info())
    print()
    print(c3.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()
