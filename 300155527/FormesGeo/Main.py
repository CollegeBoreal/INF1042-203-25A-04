from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle

def demo():
    formes = [
        Carre(4),
        Cercle(3),
        Triangle(6, 4),
    ]

    for f in formes:
        f.afficher()
        print(f"Aire:", f.aire())
        # Décommente pour dessiner (une fenêtre ou une figure Jupyter s’ouvrira)
        f.dessiner()

if __name__ == "__main__":
    demo()