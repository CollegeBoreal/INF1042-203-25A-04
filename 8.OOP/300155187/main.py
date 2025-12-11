"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [300155187]
Date : 2005-11-25
"""

from carre import Carre
from cercle import Cercle
from losange import losange
from parallelogramme import parallelogramme
from cylindre import cylindre
from prisme_carre import prisme_carre
from prisme_losange import prisme_losange
from prisme_parallelogramme import prisme_parallelogramme
from sphere import sphere
from cone import cone








def main():
    """
    Fonction principale du programme.
    Crée un carré et un cercle, puis affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

     # Création d'un losange de diagonal 10 et 8
    c3 = losange(10,8)

    # Création d'un parallelograme de diagonal 12 et 7
    c4 = parallelogramme(12,7)

     # Création d'un cylindre 
    c5 = cylindre(rayon=10,hauteur=5)

      # Création d'un prisme_carre
    c6 = prisme_carre(cote=8,hauteur=4)

    
      # Création d'un prisme_losange
    c7 = prisme_losange(d1=16,d2=8,hauteur=4)

    
      # Création d'un prisme_parallelogramme
    c8 = prisme_parallelogramme(12,6,2)

     # Création d'un sphere
    c9 = sphere(1.33)

     # Création d'un cone
    c10 = cone(0.33, 2)

    # Affichage des informations des deux figures
    print(c1.afficher_info())
    print(c2.afficher_info())
    print(c3.afficher_info())
    print(c4.afficher_info())
    print(c5.afficher_info())
    print(c6.afficher_info())
    print(c7.afficher_info())
    print(c8.afficher_info())
    print(c9.afficher_info())
    print(c10.afficher_info())







# Point d'entrée du programme
if __name__ == "__main__":
    main()