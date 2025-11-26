from figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return np.pi * (self.rayon ** 2)

    def afficher(self):
        super().afficher()
        print(f"Rayon: {self.rayon}, Aire: {self.aire():.2f}")

    def dessiner(self):
        theta = np.linspace(0, 2*np.pi, 300)
        x = self.rayon * np.cos(theta)
        y = self.rayon * np.sin(theta)
        plt.figure(figsize=(4,4))
        plt.plot(x, y, color="red")
        plt.fill(x, y, color="salmon", alpha=0.5)
        plt.axis("equal")
        plt.axis("off")
        plt.title("Cercle")
        plt.show()