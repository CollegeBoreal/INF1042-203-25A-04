"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [300155281]
Date : 2025-12-04
"""

from carre import Carre
from cercle import Cercle
from Trapeze import Trapeze

def main():
    formes = [
        Carre(4),
        Cercle(10),
        Trapeze(6, 4, 8)
    ]

    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()