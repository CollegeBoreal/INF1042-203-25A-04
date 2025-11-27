class Figure:
    """
    Classe de base pour toutes les figures géométriques.
    """

    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        return f"Figure: {self.nom}"

    def aire(self):
        raise NotImplementedError("Cette méthode doit être implémentée dans la sous-classe.")

