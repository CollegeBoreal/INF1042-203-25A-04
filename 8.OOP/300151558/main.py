"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : 300151558
Date : 2025-11-19
"""

from carre import Carre
from cercle import Cercle
from parallelogramme import Parallelogramme 

def main():
    """
    Fonction principale du programme.
    Crée un carré et un cercle, puis affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    c3 = Parallelogramme(6,4)
    
    # Affichage des informations des deux figures
    print(c1.afficher_info())
    print(c2.afficher_info())
    print(c3.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()
