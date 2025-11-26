"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [300155527]
Date : 2025-10-20
"""
from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
from Lozange import Lozange

def demo():
    formes = [
        Carre(4),
        Cercle(3),
        Triangle(6, 4),
        Lozange(8, 5)  # ✅ Nouveau
    ]

    for f in formes:
        f.afficher()
        print(f"Aire:", f.aire())
        f.dessiner()

if __name__ == "__main__":
    demo()
