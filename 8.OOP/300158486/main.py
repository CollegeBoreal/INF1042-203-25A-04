from figure import Figure
from Carre import Carre
from Cercle import Cercle
from Losange import Losange

def main():
    # Tester les classes enfants
    carre1 = Carre(4)
    cercle1 = Cercle(3)
    losange1 = Losange(6, 4)

    # Affichage
    print(carre1.afficher_info())
    print(cercle1.afficher_info())
    print(losange1.afficher_info())

    # Test de la classe Figure seule (doit produire une erreur contrôlée)
    try:
        f = Figure("FigureTest")
        print(f.aire())  # doit lever une erreur
    except Exception as e:
        print("Message attendu :", e)

if __name__ == "__main__":
    main()
