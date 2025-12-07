from figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

class Trapeze(Figure):
    def __init__(self, base1, base2, hauteur):
        super().__init__("Trapèze")
        self.base1 = base1
        self.base2 = base2
        self.hauteur = hauteur

    def aire(self):
        return ((self.base1 + self.base2) * self.hauteur) / 2

    def dessiner_3D(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        base_inf = [[0, 0, 0], [self.base1, 0, 0], [self.base1-1, self.hauteur, 0], [1, self.hauteur, 0]]
        base_sup = [[0, 0, 3], [self.base1, 0, 3], [self.base1-1, self.hauteur, 3], [1, self.hauteur, 3]]
        faces = [
            base_inf, base_sup,
            [base_inf[0], base_inf[1], base_sup[1], base_sup[0]],
            [base_inf[1], base_inf[2], base_sup[2], base_sup[1]],
            [base_inf[2], base_inf[3], base_sup[3], base_sup[2]],
            [base_inf[3], base_inf[0], base_sup[0], base_sup[3]]
        ]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='salmon', edgecolors='black', alpha=0.7))
        ax.set_title(f"Prisme trapézoïdal — base1={self.base1}, base2={self.base2}, hauteur={self.hauteur}, aire={self.aire():.2f}")
        plt.show()
