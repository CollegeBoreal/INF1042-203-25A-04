from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def main():
    carre1 = Carre(4)
    cercle1 = Cercle(3)
    triangle1 = Triangle(5, 2)

    formes = [carre1, cercle1, triangle1]

    for f in formes:
        print(f.afficher_info())

if __name__ == "__main__":
    main()

