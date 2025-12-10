from figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def dessiner_3D(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # sommets du cube
        r = [0, self.cote]
        vertices = [
            [0,0,0],[self.cote,0,0],[self.cote,self.cote,0],[0,self.cote,0],
            [0,0,self.cote],[self.cote,0,self.cote],[self.cote,self.cote,self.cote],[0,self.cote,self.cote]
        ]
        faces = [
            [vertices[0],vertices[1],vertices[2],vertices[3]],
            [vertices[4],vertices[5],vertices[6],vertices[7]],
            [vertices[0],vertices[1],vertices[5],vertices[4]],
            [vertices[2],vertices[3],vertices[7],vertices[6]],
            [vertices[1],vertices[2],vertices[6],vertices[5]],
            [vertices[4],vertices[7],vertices[3],vertices[0]]
        ]
        ax.add_collection3d(Poly3DCollection(faces, facecolors='orange', linewidths=1, edgecolors='black', alpha=0.7))
        ax.set_title(f"Cube — côté={self.cote}, aire={self.aire()}")
        plt.show()
