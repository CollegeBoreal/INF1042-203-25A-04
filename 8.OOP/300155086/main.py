"""
Fichier : main.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [300155086]
Date : 2003-07-03
"""
from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle
from Hexagone import Hexagone
from Parallelogramme import Parallelogramme

def main():
    formes = [
        Carre(4),
        Cercle(3),
        Rectangle(4, 7),
        Hexagone(6),
        Parallelogramme(5, 3),
    ]
    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()
