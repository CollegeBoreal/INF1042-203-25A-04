class Figure:
    def __init__(self, nom):
        self.nom = nom

    def aire(self):
        raise NotImplementedError("La méthode aire() doit être implémentée dans la classe dérivée.")

    def afficher(self):
        print(f"Figure: {self.nom}")