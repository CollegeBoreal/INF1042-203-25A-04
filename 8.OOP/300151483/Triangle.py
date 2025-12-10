from figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def dessiner_3D(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        vertices = [
            [0, 0, 0], [self.base, 0, 0], [self.base/2, self.hauteur, 0], [self.base/2, self.hauteur/2, 3]
        ]
        faces = [
            [vertices[0], vertices[1], vertices[2]],
            [vertices[0], vertices[1], vertices[3]],
            [vertices[1], vertices[2], vertices[3]],
            [vertices[2], vertices[0], vertices[3]]
        ]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='lightgreen', edgecolors='black', alpha=0.7))
        ax.set_title(f"Pyramide triangulaire — base={self.base}, hauteur={self.hauteur}, aire={self.aire():.2f}")
        plt.show()
