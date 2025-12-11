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

# créer le dossier images si ce n'est pas encore fait
if not os.path.exists("images"):
    os.makedirs("images")

def dessiner_et_sauvegarder(fig):
    """dessine la figure et la sauvegarde dans images/"""
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
        print(f"{f.nom} → Aire = {f.aire()}, Périmètre = {f.perimetre()}")
        dessiner_et_sauvegarder(f)

if __name__ == "__main__":
    main()
