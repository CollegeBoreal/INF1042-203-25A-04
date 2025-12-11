# Signature : BadrEddine Barragoub - 300155504

"""
Fichier : main.py
Description : Programme de test pour la classe Carré.
Auteur : 300155504
Date : 2025-12-10
"""

from carre import Carre

def main():
    carre1 = Carre(4)
    carre2 = Carre(7)

    print(carre1.afficher_info())
    print(carre2.afficher_info())

if __name__ == "__main__":
    main()

