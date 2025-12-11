"""
Fichier : main.py
Description : Point d'entrée du programme
Auteur : 300157440
Date : 2025-12-10
"""

from carre import Carre
from cercle import Cercle

def main():
    formes = [
        Carre(4),
        Cercle(3)
    ]

    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()
