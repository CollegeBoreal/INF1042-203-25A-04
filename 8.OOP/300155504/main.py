"""
Fichier : main.py
Description : Point d'entrée du programme. Test des figures géométriques.
Auteur : BADREDDINE BARRAGOUB (300155504)
Date : 2025-12-10
"""

from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
import matplotlib.pyplot as plt
import os


# créer le dossier images s'il n'existe pas
if not os.path.exists("images"):
    os.makedirs("images")


def dessiner_et_sauvegarder(fig):
    """Dessine la figure et la sauvegarde dans le dossier images/."""
    plt.figure()
    axe = plt.gca()
    fig.dessiner(axe)
    filename = f"images/{fig.nom}.png"
    plt.savefig(filename)
    plt.close()
    print(f"Image sauvegardée : {filename}")


def main():
    carre = Carre(4)
    cercle = Cercle(3)
    triangle = Triangle(5, 2)

    figures = [carre, cercle, triangle]

    for f in figures:
        print(f.afficher_info())
        dessiner_et_sauvegarder(f)


if __name__ == "__main__":
    main()
