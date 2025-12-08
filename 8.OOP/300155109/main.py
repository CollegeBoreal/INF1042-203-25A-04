"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré, un cercle et un trapeze et affiche leurs informations.
Auteur : 300155109
Date : 2025-12-07
"""

from carre import Carre
from cercle import Cercle
from trapeze import Trapeze
from hexagone import Hexagone

def main():
    # Création des figures
    f1 = Carre(4)
    f2 = Cercle(3)
    f3 = Trapeze(5, 7, 4)  # base1=5, base2=7, hauteur=4
    f4 = Hexagone(4)


    # Liste polymorphique
    formes = [f1, f2, f3, f4]

    # Affichage
    for f in formes:
        print(f.afficher_info())

# 🔥 Indispensable pour exécuter main()
if __name__ == "__main__":
    main()
