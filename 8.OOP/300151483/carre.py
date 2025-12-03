
from figure import Figure
import matplotlib.pyplot as plt

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"

    def dessiner(self):
        x = [0, self.cote, self.cote, 0, 0]
        y = [0, 0, self.cote, self.cote, 0]
        plt.figure(figsize=(5, 5))
        plt.plot(x, y, "b-")
        plt.fill(x, y, "skyblue", alpha=0.5)
        plt.title(f"Carré — côté={self.cote}, aire={self.aire()}")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
