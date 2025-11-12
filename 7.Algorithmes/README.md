## 1️⃣ Algorithme : Définition

[:tada: Participation](.scripts/Participation.md)

---

Un **algorithme** est une **suite d’instructions bien définies** permettant de résoudre un problème ou d’effectuer une tâche.

Pour construire un algorithme efficace, il faut :

1. **Stocker et organiser les données** → **structures de données**
2. **Contrôler le flux d’exécution** → **structures de contrôle**

---

## 2️⃣ Structures de données

Les **structures de données** permettent de **stocker, organiser et manipuler l’information** dans un programme. Elles sont essentielles car un algorithme dépend toujours des données qu’il traite.

### 🔹 Exemples en Python :snake:

| Structure | Utilité                       | Exemple              |
| --------- | ----------------------------- | -------------------- |
| `list`    | Séquence ordonnée, modifiable | `l = [1,2,3]`        |
| `tuple`   | Séquence ordonnée, immuable   | `t = (1,2,3)`        |
| `dict`    | Stockage clé-valeur           | `d = {"x":1, "y":2}` |
| `set`     | Ensemble non ordonné, unique  | `s = {1,2,3}`        |

### 🔹 Rôle dans l’algorithme

* Permet de **garder en mémoire des valeurs intermédiaires** (ex: somme, factorielle)
* Facilite le **parcours et la recherche** (ex: boucles sur liste ou dictionnaire)
* Structure la solution de manière **claire et efficace**

💡 Exemple : pour calculer la factorielle, on peut stocker les résultats intermédiaires dans une **liste** si on veut éviter la récursion (mémoïsation).

---

## 3️⃣ Structures de contrôle

Les **structures de contrôle** définissent le **flux d’exécution** : elles permettent de répéter, de choisir ou de sauter des instructions.

### 🔹 Types principaux

| Structure          | Utilité                  | Exemple                                 |
| ------------------ | ------------------------ | --------------------------------------- |
| `if / elif / else` | Prendre des décisions    | `if n == 0: return 1`                   |
| `for`              | Boucler sur une séquence | `for i in range(1, n+1): resultat *= i` |
| `while`            | Boucle avec condition    | `while i <= n: s += i; i += 1`          |
| `break / continue` | Contrôle fin des boucles | `if condition: break`                   |

### 🔹 Rôle dans l’algorithme

* Permet de **répéter des actions** (ex: calculs, parcours de données)
* Permet de **prendre des décisions** selon les valeurs (ex: cas de base)
* Permet de **contrôler quand arrêter** ou sauter certaines étapes

💡 Exemple :
Pour la factorielle récursive :

* La **condition de sortie** `if n == 0` est une structure de contrôle qui évite la récursion infinie.
* La multiplication `n * factorielle(n-1)` est répétée implicitement à chaque appel récursif.

---

## 4️⃣ Comment elles forment un algorithme

1. **Données → structure** : Les données doivent être **stockées et organisées** pour être accessibles et manipulables facilement.

   * Ex: liste pour parcourir les nombres, dictionnaire pour stocker des clés et valeurs.

2. **Contrôle → logique** : Les structures de contrôle définissent **l’ordre d’exécution** et permettent de **répéter, choisir, ou arrêter** certaines actions.

   * Ex: `for` pour répéter les multiplications, `if` pour le cas de base.

3. **Ensemble → algorithme** :

   * **Données structurées + instructions de contrôle** = **algorithme clair et efficace**.
   * La combinaison permet de transformer un **problème abstrait** en une **solution exécutable**.

---

### 🔹 Exemple synthétique : Factorielle itérative

```python
def factorielle(n):
    resultat = 1           # variable pour stocker le résultat
    for i in range(1,n+1): # boucle pour répéter les multiplications
        resultat *= i
    return resultat
```

* **Structure de données** : `resultat` (int)
* **Structure de contrôle** : `for` (répétition)
* **Algorithme** : calcule le produit des entiers de 1 à n

---

💡 **Conclusion** :

* Les **structures de données** définissent **ce que l’on manipule**.
* Les **structures de contrôle** définissent **comment on manipule** ces données.
* **Un algorithme est la combinaison des deux**, traduisant la logique d’un problème en instructions exécutables.

# 🐍 Résumé des instructions Python

## 1️⃣ Variables et types

| Type      | Exemple              | Description                        |
| --------- | -------------------- | ---------------------------------- |
| `int`     | `x = 5`              | Nombre entier                      |
| `float`   | `y = 2.718`          | Nombre à virgule flottante         |
| `str`     | `s = "hello"`        | Chaîne de caractères               |
| `list`    | `l = [1,2,3]`        | Liste (mutable, séquence)          |
| `tuple`   | `t = (1,2,3)`        | Tuple (immutable, séquence)        |
| `dict`    | `d = {"x":1, "y":2}` | Dictionnaire (clé-valeur)          |
| `bool`    | `b = True`           | Booléen                            |
| `bin/hex` | `0b1010, 0x1F`       | Littéraux binaires et hexadécimaux |

---

## 2️⃣ Structures de contrôle

### 🔹 Conditionnelle

```python
if condition:
    # instructions
elif autre_condition:
    # instructions
else:
    # instructions
```

### 🔹 Boucles

**For itératif :**

```python
for i in range(5):  # 0,1,2,3,4
    print(i)
```

**While :**

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

**Comprehension (compact) :**

```python
squares = [x**2 for x in range(5)]  # [0,1,4,9,16]
```

**Comprehension (fonctionnelle)**

Pour calculer la factorielle, tout en gardant l’idée d’une **condition de sortie** (cas de base).
On peut faire ça avec **`math.prod`** ou **`reduce`**, mais en gardant une syntaxe **comprehensive**.

Voici un exemple :

```python
from functools import reduce

def factorielle_comprehension(n):
    if n == 0:  # condition de sortie (cas de base)
        return 1
    # Produit de tous les entiers de 1 à n en utilisant une comprehension
    return reduce(lambda x, y: x*y, [i for i in range(1, n+1)])

# Exemple
print(factorielle_comprehension(5))  # Résultat : 120
```

### 🔹 Explication

1. **Condition de sortie** : `if n == 0: return 1` → équivalent au cas de base récursif.
2. **Comprehension** : `[i for i in range(1, n+1)]` crée la liste `[1, 2, ..., n]`.
3. **Réduction** : `reduce(lambda x, y: x*y, ...)` calcule le produit de tous les éléments, comme la récursion.

💡 Cette approche est **itérative mais proche de la récursion** dans sa logique : on multiplie tous les éléments d’une “pile” simulée par la liste.

## 3️⃣ Fonctions

**Déclaration :**

```python
def f(x):
    return x*2
```

**Récursive :**

```python
def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n-1)
```

**Itérative équivalente :**

```python
def factorielle_iter(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
```

---

## 4️⃣ Modules et imports

```python
import math
from functools import reduce
```

* `math` : fonctions mathématiques (`math.sqrt`, `math.prod`, etc.)
* `functools.reduce` : appliquer une fonction cumulativement sur une séquence

---

## 5️⃣ Structures de données avancées

* **Listes, tuples, dictionnaires** : pour stocker et manipuler des collections
* **Comprehensions** : créer des listes, dictionnaires ou ensembles de façon concise
* **Reduce / map / filter** : fonctions fonctionnelles pour traitement de séquences

---

## 6️⃣ Concepts clés vus dans les exemples

| Concept                           | Explication                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------ |
| Récursion                         | Une fonction s’appelle elle-même pour résoudre un problème de manière “définition mathématique”. |
| Boucle itérative                  | Répète un bloc d’instructions pour un nombre fixe ou jusqu’à une condition.                      |
| Cas de base / condition de sortie | Condition qui arrête la récursion ou la boucle.                                                  |
| Comprehension                     | Moyen compact et pythonique de créer des séquences ou calculer des résultats.                    |
| Accumulation                      | Stocker un résultat intermédiaire (`resultat *= i` ou `s += i`).                                 |

---

## 7️⃣ Opérations mathématiques courantes

| Opération      | Exemple                          |
| -------------- | -------------------------------- |
| Addition       | `a + b`                          |
| Soustraction   | `a - b`                          |
| Multiplication | `a * b`                          |
| Division       | `a / b`                          |
| Exponentiation | `a ** b`                         |
| Modulo         | `a % b`                          |
| Factorielle    | `math.factorial(n)` ou récursion |

---

💡 **Conseil pratique :**

* Pour **problèmes linéaires ou simples**, utilise **for / while** (itératif).
* Pour **problèmes définis par récurrence ou structures arborescentes**, la **récursion** est plus naturelle.
* Les **comprehensions** et `reduce` sont idéales pour écrire du code **compact et lisible**, mais restent itératives sous le capot.


---

## :b: Expérimentation

### 🎛️ Créer un fichier dans ce répertoire `(6.Variables)`:

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

### :rocket: Copier les fichiers :snake: Python

- [ ] Se diriger vers le répertoire avec :id: (votre identifiant boreal)
   - [ ] `cd ` :id:
- [ ] copier les fichiers sources

```sh
cp ..\.lib\* .
```

### 🔄 Exercices

#### 🧩 1️⃣ — Crée ton notebook

##### Dans Jupyter Lab

1. Ouvre ton environnement conda ou Python habituel.
2. Lance Jupyter Lab :

   ```bash
   jupyter lab
   ```
3. Clique sur ➕ `Notebook` → choisis ton environnement (ex. `INF1042-203`).
4. Sauvegarde tout de suite sous le nom :
   **`RAPPORT.ipynb`**

---

#### 🧱 2️⃣ — Structure type du rapport

Tu vas alterner **cellules Markdown** (texte explicatif) et **cellules Code** (le code à exécuter).

---

##### 🟦 **Cellule Markdown (titre principal)**

```markdown
# 🧮 Étude : Influence des boucles et de la récursion sur les algorithmes

Ce rapport démontre comment les **algorithmes** sont influencés par la **programmation itérative** (avec `for`, `while`) et la **programmation récursive** en **Python**.
```

---

##### 🟦 **Cellule Markdown**

```markdown
## 1️⃣ Factorielle

### 🔹 Formule mathématique

$
n! = \begin{cases}
   1, & \text{si } n = 0 \\
   n \times (n - 1)!, & \text{si } n > 0
\end{cases}
$
```

---

##### 🟧 **Cellule Code — Version itérative**

```python
def factorielle_iterative(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Exemple
factorielle_iterative(5)
```

---

##### 🟧 **Cellule Code — Version récursive**

```python
def factorielle_recursive(n):
    if n == 0:
        return 1
    return n * factorielle_recursive(n - 1)

# Exemple
factorielle_recursive(5)
```

---

##### 🟦 **Cellule Markdown**

```markdown
## 2️⃣ Somme des n premiers entiers

### 🔹 Formule mathématique

$
S(n) = 1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}
$

### 🔹 Forme récursive

$
S(n) =
\begin{cases}
   0, & \text{si } n = 0 \\
   n + S(n - 1), & \text{si } n > 0
\end{cases}
$
```

---

##### 🟧 **Cellule Code — Version itérative (while)**

```python
def somme_while(n):
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    return s

somme_while(5)
```

---

##### 🟧 **Cellule Code — Version récursive**

```python
def somme_recursive(n):
    if n == 0:
        return 0
    return n + somme_recursive(n - 1)

somme_recursive(5)
```

---

##### 🟦 **Cellule Markdown**

```markdown
## 3️⃣ Suite de Fibonacci

### 🔹 Formule mathématique

$
F(n) =
\begin{cases}
   0, & \text{si } n = 0 \\
   1, & \text{si } n = 1 \\
   F(n - 1) + F(n - 2), & \text{si } n \ge 2
\end{cases}
$
```

---

##### 🟧 **Cellule Code — Version itérative**

```python
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

fib_iter(10)
```

---

##### 🟧 **Cellule Code — Version récursive**

```python
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

fib_rec(10)
```

---

##### 🟦 **Cellule Markdown (Synthèse)**

```markdown
## 📘 4️⃣ Synthèse comparative

| Algorithme | Formule mathématique | Base | Récurrence | Complexité temporelle |
|-------------|----------------------|-------|-------------|------------------------|
| Factorielle | \\( n! = n \times (n-1)! \\) | \\( 0! = 1 \\) | Simple | O(n) |
| Somme | \\( S(n) = n + S(n-1) \\) | \\( S(0) = 0 \\) | Simple | O(n) |
| Fibonacci | \\( F(n) = F(n-1) + F(n-2) \\) | \\( F(0)=0, F(1)=1 \\) | Double | O($2^n$) (récursif) / O(n) (itératif) |

---

### 🧠 Conclusion

- Les **boucles (`for`, `while`)** permettent une **programmation itérative**, efficace en mémoire.  
- La **récursion** traduit directement la **définition mathématique** d’un algorithme, mais consomme plus de mémoire.  
- Les deux approches atteignent le même résultat, mais influencent différemment la **structure, la performance et la lisibilité** des algorithmes.
```

---

#### ✅ Résumé visuel

| Type de cellule | Contenu                                                              |
| --------------- | -------------------------------------------------------------------- |
| 🟦 Markdown     | Titre, explications, formules mathématiques                          |
| 🟧 Code         | Fonctions Python avec exemples (`factorielle`, `somme`, `fibonacci`) |

