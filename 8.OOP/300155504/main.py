"""
Projet POO — Figures géométriques
Auteur      : BADREDDINE BARRAGOUB
Matricule   : 300155504
Fichier     : main.py
Description : Programme principal permettant de créer et dessiner les figures.
"""

__author__ = "BADREDDINE BARRAGOUB"
__student_id__ = "300155504"

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
    print(f"Image sauvegardée : {filename}")

    plt.close()


def main():
    carre = Carre(5)
    cercle = Cercle(4)
    triangle = Triangle(6, 4)

    figures = [carre, cercle, triangle]

    for f in figures:
        print(f"{f.nom} → aire = {f.aire():.2f}, périmètre = {f.perimetre():.2f}")
        dessiner_et_sauvegarder(f)


if __name__ == "__main__":
    main()
