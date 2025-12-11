# 🧮 Étude : Influence des boucles et de la récursion sur les algorithmes

|       |                       |
|-------|-----------------------|
| 👤 Nom | **Maimouna Diallo**   |
| 🆔 ID  | **300155187**         |

Ce rapport présente une analyse de la façon dont la **programmation itérative** (`for`, `while`) et la **programmation récursive** influencent le fonctionnement et la performance des algorithmes en Python.

---

## 1️⃣ Factorielle

### 🔹 Version itérative
```python
def factorielle_iterative(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Exemple
factorielle_iterative(5)
Résultat : 120
🔹 Version récursive
def factorielle_recursive(n):
    if n == 0:
        return 1
    return n * factorielle_recursive(n - 1)

# Exemple
factorielle_recursive(5)
Résultat : 120

🔹 Version fonctionnelle (reduce + compréhension)
from functools import reduce

def factorielle_comprehension(n):
    if n == 0:
        return 1
    return reduce(lambda x, y: x*y, [i for i in range(1, n+1)])
2️⃣ Somme des n premiers entiers

🔹 Formule mathématique
## 🔢 Somme des n premiers entiers

### 📌 Formule mathématique

$$
S(n) = 1 + 2 + 3 + \ldots + n = \frac{n(n+1)}{2}
$$

---

### 🔄 Forme récursive

$$
S(n)=
\begin{cases}
0, & \text{si } n = 0 \\
n + S(n-1), & \text{si } n > 0
\end{cases}
$$

---

### 🌀 Version itérative (while)

```python
def somme_n(n):
    s = 0
    i = 1
    while i <= n:
        s += i
        i += 1
    return s
🔹 Version itérative (while)
def somme_while(n):
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    return s

somme_while(5)
Résultat : 15
🔹 Version récursive
def somme_recursive(n):
    if n == 0:
        return 0
    return n + somme_recursive(n - 1)

somme_recursive(5)
Résultat : 15
3️⃣ Suite de Fibonacci
🔹 Formule mathématique

<img width="691" height="187" alt="image" src="https://github.com/user-attachments/assets/b1a40af9-71b1-438f-bd8a-61cedfee7eee" />


🔹 Version itérative

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

fib_rec(10)
Résultat : 55

📘 4️⃣ Synthèse comparative

| Algorithme      | Base             | Type de récursion | Complexité                                   |
| --------------- | ---------------- | ----------------- | -------------------------------------------- |
| **Factorielle** | `0! = 1`         | Simple            | **O(n)**                                     |
| **Somme**       | `S(0) = 0`       | Simple            | **O(n)**                                     |
| **Fibonacci**   | `F(0)=0, F(1)=1` | Double            | **O(2ⁿ)** (récursive) / **O(n)** (itérative) |

🧠 Conclusion

Les boucles (for, while) permettent une approche itérative, rapide et efficace en mémoire.

La récursion correspond directement à la définition mathématique, mais peut devenir plus coûteuse en mémoire.

Les deux méthodes produisent les mêmes résultats, mais influencent différemment :

la structure du code,

la performance,

et la lisibilité des algorithmes.

✨ Ce travail met en lumière l’importance de choisir la bonne approche selon les besoins et les contraintes de l’algorithme.




