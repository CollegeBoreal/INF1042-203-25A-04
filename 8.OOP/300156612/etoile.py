# etoile.py
from figure import Figure
import math

class Etoile(Figure):
    def __init__(self, points=5, step=2, rayon=100):
        self.points = points
        self.step = step
        self.rayon = rayon

    def afficher_info(self):
        return f"Figure: Etoile, points={self.points}, step={self.step}, rayon={self.rayon}"

    def dessiner(self, t):
        sommets = []

        for i in range(self.points):
            angle = 2 * math.pi * i / self.points
            x = self.rayon * math.cos(angle)
            y = self.rayon * math.sin(angle)
            sommets.append((x, y))

        t.penup()
        t.goto(sommets[0])
        t.pendown()

        pos = 0
        for _ in range(self.points):
            t.goto(sommets[pos])
            pos = (pos + self.step) % self.points
