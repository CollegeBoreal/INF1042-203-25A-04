from carre import Carre
from cercle import Cercle
from Triangle import Triangle
from trapeze import Trapeze   # <-- ajout

def main():
    formes = [
        Carre(4),
        Cercle(3),
        Triangle(5, 2),
        Trapeze(6, 4, 3)   # <-- exemple de trapèze
    ]

    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()
