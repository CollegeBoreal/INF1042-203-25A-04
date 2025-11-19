
## **Projet Python : Formes Geométriques**

### **Structure du projet**

```
[:id:]/
│
├── main.py        # Point d'entrée du programme
├── figure.py      # Classe de base Figure
├── Carre.py       # Classe Carré
└── Cercle.py      # Classe Cercle
```

---

### **1. Fichier `figure.py`**

```python
class Figure:
    def __init__(self, nom):
        self.nom = nom

    def afficher_info(self):
        return f"Figure: {self.nom}"

    def aire(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")
```

---

### **2. Fichier `Carre.py`**

```python
from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")
        self.cote = cote

    def aire(self):
        return self.cote ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"
```

---

### **3. Fichier `Cercle.py`**

```python
from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def afficher_info(self):
        return f"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}"
```

---

### **4. Fichier `main.py`**

```python
from Carre import Carre
from Cercle import Cercle

def main():
    # Créer les figures
    c1 = Carre(4)
    c2 = Cercle(3)

    # Afficher leurs informations
    print(c1.afficher_info())
    print(c2.afficher_info())

if __name__ == "__main__":
    main()
```

---

### **Points pédagogiques couverts**

* **Variables** : `cote`, `rayon`
* **Fonctions** : `main()`, `aire()`, `afficher_info()`
* **Modules** : import séparé depuis `Carre.py` et `Cercle.py`
* **POO et héritage** : `Figure` → `Carre` / `Cercle`
* **Point d’entrée** : `if __name__ == "__main__": main()`


