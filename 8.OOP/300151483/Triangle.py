from figure import Figure
import matplotlib.pyplot as plt

class Triangle(Figure):
    def __init__(self, base, hauteur):
        super().__init__("Triangle")
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2

    def afficher_info(self):
        return f"{super().afficher_info()}, base={self.base}, hauteur={self.hauteur}, aire={self.aire()}"

    def dessiner(self):
        x = [0, self.base, self.base/2, 0]
        y = [0, 0, self.hauteur, 0]
        plt.figure(figsize=(5, 5))
        plt.plot(x, y, "g-")
        plt.fill(x, y, "lightgreen", alpha=0.5)
        plt.title(f"Triangle — base={self.base}, hauteur={self.hauteur}, aire={self.aire()}")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
