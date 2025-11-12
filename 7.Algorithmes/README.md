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

---

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

## 📘 Structure complète du `RAPPORT.ipynb`

---

### 🟦 **Cellule Markdown (titre principal)**

```markdown
# 🧮 Étude : Influence des boucles et de la récursion sur les algorithmes

Ce rapport démontre comment les **algorithmes** sont influencés par la **programmation itérative** (avec `for`, `while`) et la **programmation récursive** en **Python**.
```

---

### 🟦 **Cellule Markdown**

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

### 🟧 **Cellule Code — Version itérative**

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

### 🟧 **Cellule Code — Version récursive**

```python
def factorielle_recursive(n):
    if n == 0:
        return 1
    return n * factorielle_recursive(n - 1)

# Exemple
factorielle_recursive(5)
```

---

### 🟦 **Cellule Markdown**

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

### 🟧 **Cellule Code — Version itérative (while)**

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

### 🟧 **Cellule Code — Version récursive**

```python
def somme_recursive(n):
    if n == 0:
        return 0
    return n + somme_recursive(n - 1)

somme_recursive(5)
```

---

### 🟦 **Cellule Markdown**

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

### 🟧 **Cellule Code — Version itérative**

```python
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

fib_iter(10)
```

---

### 🟧 **Cellule Code — Version récursive**

```python
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

fib_rec(10)
```

---

### 🟦 **Cellule Markdown (Synthèse)**

```markdown
## 📘 4️⃣ Synthèse comparative

| Algorithme | Formule mathématique | Base | Récurrence | Complexité temporelle |
|-------------|----------------------|-------|-------------|------------------------|
| Factorielle | \\( n! = n \\times (n-1)! \\) | \\( 0! = 1 \\) | Simple | O(n) |
| Somme | \\( S(n) = n + S(n-1) \\) | \\( S(0) = 0 \\) | Simple | O(n) |
| Fibonacci | \\( F(n) = F(n-1) + F(n-2) \\) | \\( F(0)=0, F(1)=1 \\) | Double | O(2^n) (récursif) / O(n) (itératif) |

---

### 🧠 Conclusion

- Les **boucles (`for`, `while`)** permettent une **programmation itérative**, efficace en mémoire.  
- La **récursion** traduit directement la **définition mathématique** d’un algorithme, mais consomme plus de mémoire.  
- Les deux approches atteignent le même résultat, mais influencent différemment la **structure, la performance et la lisibilité** des algorithmes.
```

---

### ✅ Résumé visuel

| Type de cellule | Contenu                                                              |
| --------------- | -------------------------------------------------------------------- |
| 🟦 Markdown     | Titre, explications, formules mathématiques                          |
| 🟧 Code         | Fonctions Python avec exemples (`factorielle`, `somme`, `fibonacci`) |

