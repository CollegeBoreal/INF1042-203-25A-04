"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : 300155504
Date : 2025-12-11
"""

from Carre import Carre
from Cercle import Cercle
# from Triangle import Triangle  # ← يمكن تستعمله فالتجارب فقط

def main():
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    # Affichage des informations
    print(c1.afficher_info())
    print(c2.afficher_info())

if __name__ == "__main__":
    main()
