

🧮 Étude : Figures Géométriques — Aires et Visualisations

Nom : Hind Chili
ID : 300151558

📘 Introduction

Ce travail présente l’utilisation de la Programmation Orientée Objet (POO) en Python pour modéliser et visualiser des figures géométriques simples en 2D.
Nous utilisons :

une classe de base Figure,

et trois classes dérivées : Carre, Cercle, Parallelogramme.

L’objectif est de :

définir des classes permettant de calculer l’aire de chaque figure,

créer des objets géométriques,

afficher graphiquement les formes dans un repère cartésien à l’aide de :

matplotlib 3.9.2

numpy 2.1.3

🏗️ 1. Hiérarchie des classes
🔹 Figure (classe de base)

Contient :

un attribut nom,

une méthode afficher_info(),

une méthode abstraite aire() que chaque figure doit redéfinir.

🔹 Carre

Attribut : cote
Formule de l’aire :

𝐴
=
𝑐
𝑜
^
𝑡
𝑒
ˊ
2
A=c
o
^
t
e
ˊ
2
🔹 Cercle

Attribut : rayon
Formule de l’aire :

𝐴
=
𝜋
𝑟
2
A=πr
2
🔹 Parallélogramme

Attributs : base, hauteur
Formule de l’aire :

𝐴
=
𝑏
𝑎
𝑠
𝑒
×
ℎ
𝑎
𝑢
𝑡
𝑒
𝑢
𝑟
A=base×hauteur
📂 2. Importation des classes
from carre import Carre
from cercle import Cercle
from parallelogramme import Parallelogramme


Création des objets :

c1 = Carre(4)
c2 = Cercle(3)
c3 = Parallelogramme(6, 4)

📊 3. Fonctions d’affichage graphique

Les visualisations utilisent matplotlib pour tracer des figures proportionnelles et remplir leur intérieur pour une meilleure lisibilité.

⬜ Affichage du Carré
def afficher_carre(carre):
    cote = carre.cote
    x = [0, cote, cote, 0, 0]
    y = [0, 0, cote, cote, 0]

    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Carré — côté={cote}, aire={carre.aire()}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

⚪ Affichage du Cercle
def afficher_cercle(cercle):
    r = cercle.rayon
    theta = np.linspace(0, 2*np.pi, 300)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Cercle — rayon={r}, aire={cercle.aire():.2f}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

⬛ Affichage du Parallélogramme
def afficher_parallelogramme(parallelogramme):
    base = parallelogramme.base
    hauteur = parallelogramme.hauteur

    x = [0, base, base + 1.5, 1.5, 0]   # Inclinaison
    y = [0, 0, hauteur, hauteur, 0]

    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)

    plt.title(
        f"Parallélogramme – Base={base}, Hauteur={hauteur}, Aire={parallelogramme.aire()}"
    )

    plt.axis("equal")
    plt.grid(True)
    plt.show()

🧪 4. Résultats — Exécution des affichages
afficher_carre(c1)
afficher_cercle(c2)
afficher_parallelogramme(c3)


Chaque fonction :

trace la figure,

applique un remplissage semi-transparent,

affiche une grille,

calcule et montre l’aire de la figure.

Ces visualisations permettent de comprendre la géométrie tout en pratiquant la POO et la programmation scientifique.

🎯 Conclusion

Dans ce projet, nous avons réussi à :
✔ mettre en place une hiérarchie de classes en Python
✔ implémenter des méthodes de calcul d’aire
✔ utiliser matplotlib pour visualiser des figures géométriques
✔ manipuler des objets et fonctions dans un notebook
