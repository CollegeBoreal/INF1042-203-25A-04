from figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}"

    def dessiner(self):
        theta = np.linspace(0, 2*math.pi, 300)
        x = self.rayon * np.cos(theta)
        y = self.rayon * np.sin(theta)
        plt.figure(figsize=(5, 5))
        plt.plot(x, y, "r-")
        plt.fill(x, y, "lightcoral", alpha=0.5)
        plt.title(f"Cercle — rayon={self.rayon}, aire={self.aire():.2f}")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
