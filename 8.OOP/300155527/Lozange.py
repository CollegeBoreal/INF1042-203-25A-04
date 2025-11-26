from figure import Figure
import matplotlib.pyplot as plt

class Lozange(Figure):
    def __init__(self, diagonale1, diagonale2):
        super().__init__("Lozange")
        self.diagonale1 = diagonale1
        self.diagonale2 = diagonale2

    def aire(self):
        # Formule : (d1 * d2) / 2
        return (self.diagonale1 * self.diagonale2) / 2

    def afficher(self):
        super().afficher()
        print(f"Diagonale 1: {self.diagonale1}, Diagonale 2: {self.diagonale2}, Aire: {self.aire()}")

    def dessiner(self):
        # Points du lozange centrés sur l'origine
        x = [0, self.diagonale1/2, 0, -self.diagonale1/2, 0]
        y = [self.diagonale2/2, 0, -self.diagonale2/2, 0, self.diagonale2/2]

        plt.figure(figsize=(4,4))
        plt.plot(x, y, color="purple")
        plt.fill(x, y, color="violet", alpha=0.5)
        plt.axis("equal")
        plt.axis("off")
        plt.title("Lozange")
        plt.show()
