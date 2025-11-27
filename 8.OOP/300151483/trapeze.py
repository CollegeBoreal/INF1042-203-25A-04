
from figure import Figure
import matplotlib.pyplot as plt

class Trapeze(Figure):
    def __init__(self, base1, base2, hauteur):
        super().__init__("Trapèze")
        self.base1 = base1
        self.base2 = base2
        self.hauteur = hauteur

    def aire(self):
        return ((self.base1 + self.base2) * self.hauteur) / 2

    def afficher_info(self):
        return f"{super().afficher_info()}, base1={self.base1}, base2={self.base2}, hauteur={self.hauteur}, aire={self.aire()}"

    def dessiner(self):
        x = [0, self.base1, self.base2, 0, 0]
        y = [0, 0, self.hauteur, self.hauteur, 0]
        plt.figure(figsize=(5, 5))
        plt.plot(x, y, "m-")
        plt.fill(x, y, "violet", alpha=0.5)
        plt.title(f"Trapèze — base1={self.base1}, base2={self.base2}, hauteur={self.hauteur}, aire={self.aire()}")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
