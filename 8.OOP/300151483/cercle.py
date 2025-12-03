from figure import Figure
import numpy as np
import matplotlib.pyplot as plt

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return np.pi * self.rayon**2

    def dessiner_3D(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
        x = self.rayon * np.cos(u) * np.sin(v)
        y = self.rayon * np.sin(u) * np.sin(v)
        z = self.rayon * np.cos(v)
        ax.plot_surface(x, y, z, color='lightblue', alpha=0.6)
        ax.set_title(f"Sphère — rayon={self.rayon}, aire={self.aire():.2f}")
        plt.show()
