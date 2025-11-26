from figure import Figure
import matplotlib.pyplot as plt

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher(self):
        super().afficher()
        print(f"Côté: {self.cote}, Aire: {self.aire()}")

    def dessiner(self):
        x = [0, self.cote, self.cote, 0, 0]
        y = [0, 0, self.cote, self.cote, 0]
        plt.figure(figsize=(4,4))
        plt.plot(x, y, color="green")
        plt.fill(x, y, color="lightgreen", alpha=0.5)
        plt.axis("equal")
        plt.axis("off")
        plt.title("Carré")
        plt.show()