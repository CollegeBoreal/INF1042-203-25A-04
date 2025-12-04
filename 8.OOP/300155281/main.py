"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [300155281]
Date : YYYY-MM-DD
"""

from Carre import Carre
from Cercle import Cercle
from Trapeze import Trapeze

def main():
    formes = [
        Carre(4),
        Cercle(3),
        Trapeze(6, 4, 3)
    ]

    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()
