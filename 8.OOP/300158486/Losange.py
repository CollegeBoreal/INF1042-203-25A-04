from figure import Figure

class Losange(Figure):
    def __init__(self, d1, d2):
        super().__init__("Losange")
        self.d1 = d1
        self.d2 = d2

    def aire(self):
        return (self.d1 * self.d2) / 2

    def afficher_info(self):
        info = super().afficher_info()
        info += f", d1={self.d1}"
        info += f", d2={self.d2}"
        info += f", aire={self.aire()}"
        return info