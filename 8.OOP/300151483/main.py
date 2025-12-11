from carre import Carre
from cercle import Cercle
from Triangle import Triangle
from trapeze import Trapeze

def main():
    formes = [
        Carre(4),
        Cercle(3),
        Triangle(5, 2),
        Trapeze(6, 4, 3)
    ]

    for f in formes:
        print(f.afficher_info())
        f.dessiner_3D()   # ⚠️ utiliser la version 3D

if __name__ == "__main__":
    main()
