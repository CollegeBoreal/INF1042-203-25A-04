"""
Fichier : main.py
Description : Point d'entrée du programme : teste les classes géométriques
Auteur : 300158486
Date : 2025-11-25
"""

from figure import Figure
from Carre import Carre
from Cercle import Cercle
from Etoile import Etoile

def main():
    # Tester les classes enfants
    carre1 = Carre(4)
    cercle1 = Cercle(3)
    etoile1 = Etoile(5)

    print(carre1.afficher_info())
    print(cercle1.afficher_info())
    print(etoile1.afficher_info())

    # Tester Figure seule (doit lever une erreur)
    try:
        f = Figure("FigureTest")
        print(f.aire())  # Normalement erreur -> méthode abstraite
    except Exception as e:
        print("Message attendu :", e)

if __name__ == "__main__":
    main()