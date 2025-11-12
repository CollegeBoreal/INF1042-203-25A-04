# 📘 Structure complète du `RAPPORT.ipynb`

---

## 🟦 **Cellule Markdown (titre principal)**

```markdown
# 🧮 Étude : Influence des boucles et de la récursion sur les algorithmes

Ce rapport démontre comment les **algorithmes** sont influencés par la **programmation itérative** (avec `for`, `while`) et la **programmation récursive** en **Python**.
```

---

## 🟦 **Cellule Markdown**

```markdown
## 1️⃣ Factorielle

### 🔹 Formule mathématique

\\[
n! =
\\begin{cases}
1, & \\text{si } n = 0 \\\\
n \\times (n - 1)!, & \\text{si } n > 0
\\end{cases}
\\]
```

---

## 🟧 **Cellule Code — Version itérative**

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

## 🟧 **Cellule Code — Version récursive**

```python
def factorielle_recursive(n):
    if n == 0:
        return 1
    return n * factorielle_recursive(n - 1)

# Exemple
factorielle_recursive(5)
```

---

## 🟦 **Cellule Markdown**

```markdown
## 2️⃣ Somme des n premiers entiers

### 🔹 Formule mathématique

\\[
S(n) = 1 + 2 + 3 + \\dots + n = \\frac{n(n + 1)}{2}
\\]

### 🔹 Forme récursive

\\[
S(n) =
\\begin{cases}
0, & \\text{si } n = 0 \\\\
n + S(n - 1), & \\text{si } n > 0
\\end{cases}
\\]
```

---

## 🟧 **Cellule Code — Version itérative (while)**

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

## 🟧 **Cellule Code — Version récursive**

```python
def somme_recursive(n):
    if n == 0:
        return 0
    return n + somme_recursive(n - 1)

somme_recursive(5)
```

---

## 🟦 **Cellule Markdown**

```markdown
## 3️⃣ Suite de Fibonacci

### 🔹 Formule mathématique

\\[
F(n) =
\\begin{cases}
0, & \\text{si } n = 0 \\\\
1, & \\text{si } n = 1 \\\\
F(n - 1) + F(n - 2), & \\text{si } n \\ge 2
\\end{cases}
\\]
```

---

## 🟧 **Cellule Code — Version itérative**

```python
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

fib_iter(10)
```

---

## 🟧 **Cellule Code — Version récursive**

```python
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

fib_rec(10)
```

---

## 🟦 **Cellule Markdown (Synthèse)**

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

## ✅ Résumé visuel

| Type de cellule | Contenu                                                              |
| --------------- | -------------------------------------------------------------------- |
| 🟦 Markdown     | Titre, explications, formules mathématiques                          |
| 🟧 Code         | Fonctions Python avec exemples (`factorielle`, `somme`, `fibonacci`) |

