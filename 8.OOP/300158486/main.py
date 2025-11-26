"""
Fichier : main.py
Description : Point d'entrée du programme : teste les classes géométriques
Auteur : 300158486
Date : 2025-11-25
"""

from figure import Figure
from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle

def main():
    # Tester les classes enfants
    carre1 = Carre(4)
    cercle1 = Cercle(3)
    rectangle1 = Rectangle(5, 2)

    print(carre1.afficher_info())
    print(cercle1.afficher_info())
    print(rectangle1.afficher_info())

    # Tester Figure seule (donne erreur car aire n’est pas implémenté)
    try:
        f = Figure("FigureTest")
        print(f.aire())  # Normalement erreur → méthode abstraite
    except Exception as e:
        print("Message attendu :", e)

if __name__ == "__main__":
    main()