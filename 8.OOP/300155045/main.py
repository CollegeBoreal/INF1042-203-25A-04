"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré, un cercle et un triangle,
              puis affiche leurs informations.
Auteur : 300155045
Date : 2025-10-10
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle  


def main():
    """
    Fonction principale du programme.
    Crée un carré, un cercle et un triangle, puis affiche leurs informations.
    """
    c1 = Carre(4)

    c2 = Cercle(3)

    t1 = Triangle(5, 2)

    formes = [c1, c2, t1]

    for f in formes:
        print(f.afficher_info())
        print(f"Aire: {f.aire()} 📏")

if __name__ == "__main__":
    main()
