"""
Fichier : main.py
Description : Point d'entrée du programme.
Crée un carré, un cercle et un triangle et affiche leurs informations.
Auteur : [300155606]
Date : 2025-11-26
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():
    """ Fonction principale du programme. """

    # Création d’un carré
    c1 = Carre(4)

    # Création d’un cercle
    c2 = Cercle(3)

    # Création d’un triangle équilatéral
    t1 = Triangle(5)

    # Affichage des informations
    print(c1.afficher_info())
    print(c2.afficher_info())
    print(t1.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()
