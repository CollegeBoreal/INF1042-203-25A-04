from figure import Figure
import matplotlib.pyplot as plt

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def afficher(self):
        super().afficher()
        print(f"Base: {self.base}, Hauteur: {self.hauteur}, Aire: {self.aire()}")

    def dessiner(self):
        # Triangle isocèle basé sur l’axe x
        x = [0, self.base/2, self.base, 0]
        y = [0, self.hauteur, 0, 0]
        plt.figure(figsize=(4,4))
        plt.plot(x, y, color="blue")
        plt.fill(x, y, color="skyblue", alpha=0.5)
        plt.axis("equal")
        plt.axis("off")
        plt.title("Triangle")
        plt.show()