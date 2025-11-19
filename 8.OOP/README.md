# OOP

---

## :b: Expérimentation

### 🎛️ Créer un fichier dans ce répertoire `(8.OOP)`:

:checkered_flag: Finalement,

- [ ] Créer un répertoire avec :id: (votre identifiant boreal)
   - [ ] `mkdir ` :id:
- [ ] dans votre répertoire ajouter le fichier `README.md`
  - [ ] `nano `README.md
- [ ] envoyer vers le serveur `github.com`
  - [ ] `cd ..`
  - [ ] `git add `:id: 
  - [ ] `git commit -m "mon fichier ..."`
  - [ ] `git push`

- [ ] Se diriger vers le répertoire avec :id: (votre identifiant boreal)
   - [ ] `cd ` :id:

- [ ] Continuer les 🔄 Exercices 

### 🔄 Exercices

#### 🧩 **Projet Python : Gestion de figures géométriques**

Objectif : Créer un programme Python qui définit des figures géométriques de base et des figures héritées, démontrant l’héritage et la POO (Programmation Orientée Objet).

##### **0. Structure du projet**

```
[:id:]/
│
├── README.md        # Le fichier de documentation
├── images/.gitkeep  # Le fichier permettant de garder le répertoire images
├── main.py          # Point d'entrée du programme
├── figure.py        # Classe de base Figure
├── Carre.py         # Classe Carré
└── Cercle.py        # Classe Cercle
```

---

##### **1. Fichier `figure.py`**

```python
"""
Fichier : figure.py
Description : Classe de base pour toutes les figures géométriques
Auteur : [ID de l'étudiant]
Date : YYYY-MM-DD
"""

class Figure:
    def __init__(self, nom):
        # Nom de la figure (ex: Carré, Cercle)
        self.nom = nom

    def afficher_info(self):
        # Retourne une chaîne contenant le nom de la figure
        return f"Figure: {self.nom}"

    def aire(self):
        # Méthode à implémenter par les sous-classes
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")
```

---

##### **2. Fichier `Carre.py`**

```python
"""
Fichier : Carre.py
Description : Classe Carré héritant de Figure
Auteur : [ID de l'étudiant]
Date : YYYY-MM-DD
"""

from figure import Figure

class Carre(Figure):
    def __init__(self, cote):
        super().__init__("Carré")  # Appel du constructeur de la classe de base
        self.cote = cote           # Longueur du côté du carré

    def aire(self):
        # Calcul de l'aire du carré
        return self.cote ** 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, le côté et l'aire
        return f"{super().afficher_info()}, côté={self.cote}, aire={self.aire()}"
```

---

##### **3. Fichier `Cercle.py`**

```python
"""
Fichier : Cercle.py
Description : Classe Cercle héritant de Figure
Auteur : [ID de l'étudiant]
Date : YYYY-MM-DD
"""

from figure import Figure
import math

class Cercle(Figure):
    def __init__(self, rayon):
        super().__init__("Cercle")  # Appel du constructeur de la classe de base
        self.rayon = rayon           # Rayon du cercle

    def aire(self):
        # Calcul de l'aire du cercle
        return math.pi * self.rayon ** 2

    def afficher_info(self):
        # Retourne une chaîne contenant le nom, le rayon et l'aire
        return f"{super().afficher_info()}, rayon={self.rayon}, aire={self.aire():.2f}"
```

---

##### **4. Fichier `main.py`**

```python
"""
Fichier : main.py
Description : Point d'entrée du programme. Crée un carré et un cercle et affiche leurs informations.
Auteur : [ID de l'étudiant]
Date : YYYY-MM-DD
"""

from Carre import Carre
from Cercle import Cercle

def main():
    """
    Fonction principale du programme.
    Crée un carré et un cercle, puis affiche leurs informations.
    """
    # Création d'un carré de côté 4
    c1 = Carre(4)

    # Création d'un cercle de rayon 3
    c2 = Cercle(3)

    # Affichage des informations des deux figures
    print(c1.afficher_info())
    print(c2.afficher_info())

# Point d'entrée du programme
if __name__ == "__main__":
    main()
```

---

##### **Points pédagogiques couverts**

* **Variables** : `cote`, `rayon`
* **Fonctions** : `main()`, `aire()`, `afficher_info()`
* **Modules** : import séparé depuis `Carre.py` et `Cercle.py`
* **POO et héritage** : `Figure` → `Carre` / `Cercle`
* **Point d’entrée** : `if __name__ == "__main__": main()`

✅ **Bénéfices des en-têtes :**

* Chaque fichier est **identifiable rapidement**.
* Les étudiants comprennent **la fonction et le contenu de chaque module**.
* Facilite la maintenance et le suivi dans des projets plus grands.


