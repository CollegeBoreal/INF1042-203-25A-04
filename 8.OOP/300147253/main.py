from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle  # <- ajouter cette ligne

def main():
    c1 = Carre(4)
    c2 = Cercle(3)
    t1 = Triangle(5, 2)  # <- créer un triangle

    print(c1.afficher_info())
    print(c2.afficher_info())
    print(t1.afficher_info())  # <- afficher les infos du triangle

if __name__ == "__main__":
    main()

