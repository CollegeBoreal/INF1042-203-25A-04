class Parallelogramme:
    def __init__(self, base, hauteur, angle):
        self.base = base
        self.hauteur = hauteur
        self.angle = angle   # 🔥 Ajouter l’angle !!

    def aire(self):
        return self.base * self.hauteur

    def afficher_info(self):
        return (f"Parallélogramme : base={self.base}, hauteur={self.hauteur}, angle={self.angle}, "
                f"aire={self.aire()}")
