```markdown
# 🪐 RAPPORT : Analyse de Code Python (Variables, Moyennes, Ensembles)

### Nom: Personne Importante 
### 🆔 : 999999999
|     |                     |
| --- | ------------------- |
| Nom | Personne Importante |
| 🆔  | 999999999           |


Ce notebook présente trois sections :
1. Le module `embellisseur` et la fonction `f`
2. Le module `moyenne` (moyenne algébrique et géométrique)
3. Les ensembles (`set`) et la compréhension
```

---

##### 🟩 Cellule Markdown (section 1 : explication)

```markdown
#### 1️⃣ Import du module `embellisseur`

Cette section montre comment la fonction `f` traite différents types de variables.
Elle illustre le **polymorphisme** de Python (une même fonction peut gérer plusieurs types).
```

---

##### 🟧 Cellule Code

```python
from embellisseur import f

exemples = [
    10,
    2.718,
    "hello",
    [7, 8, 9],
    (10, 20, 30),
    {"x": 1, "y": 2}
]

for e in exemples:
    print(f"\n--- f({e}) ---")
    resultat = f(e)
    for k, v in resultat.items():
        print(f"{k:12} -> {v}")
```

---

##### 🟩 Cellule Markdown (section 2)

```markdown
## 2️⃣ Moyenne algébrique et géométrique

Le module `moyenne` contient deux fonctions :

- `algebrique(L)` : calcule la moyenne arithmétique  
  $
  \bar{x} = \frac{\sum x_i}{n}
  $
- `geometrique(L)` : calcule la moyenne géométrique  
  $
  G = \sqrt[n]{\prod x_i}
  $
```

---

##### 🟧 Cellule Code

```python
from moyenne import algebrique, geometrique

print("La moyenne algébrique est :", algebrique([2, 4.5, 6, 8, 10]))
print("La moyenne géométrique est :", geometrique([2, 4.5, 6, 8, 10]))
```

---

##### 🟩 Cellule Markdown (section 3)

```markdown
## 3️⃣ Ensembles (set) et compréhension

${\displaystyle \{(k,x)\ \|\ k\in K\wedge x\in X\wedge P(x)\}}$

On construit un ensemble `S` de couples `(k, x)` où :
- `k` provient de la liste `K = ['A', 'B', 'C']`
- `x` provient de la liste `X = [1, 2, 3, 4, 5, 6]`
- et `x` satisfait une condition `P(x)` (ici, être pair).

Cela illustre :
- les **comprehensions** (`{... for ... if ...}`)
- l'utilisation des **ensembles (`set`)**
- la **réutilisation de fonction** (`algebrique`)
```

---

##### 🟧 Cellule Code

```python
K = ['A', 'B', 'C']
X = [1, 2, 3, 4, 5, 6]

def P(x):
    return x % 2 == 0

S = {(k, x) for k in K for x in X if P(x)}
print("Ensemble des couples filtrés :", S)

x_values = [x for (_, x) in S]
if x_values:
    moyenne = algebrique(x_values)
else:
    moyenne = 0

print("Moyenne algébrique des x filtrés :", moyenne)
```

---

##### 🟩 Cellule Markdown (conclusion)

```markdown
## 🧠 Conclusion

Ce rapport montre comment :
- Une même fonction (`f`) peut traiter plusieurs types de données.
- Des fonctions mathématiques (`algebrique`, `geometrique`) peuvent être réutilisées.
- Les **ensembles** et **comprehensions** facilitent les filtres et combinaisons de données.

> 🧩 Python est un langage à typage dynamique, où les fonctions peuvent être générales,
> et les structures (listes, tuples, sets, dictionnaires) très expressives.
```

---

#### ✅ 3️⃣ — Conseils de mise en forme

* 🔤 Utilise **les titres Markdown** (`#`, `##`, `###`) pour structurer.
* 🧮 Pour des formules, mets-les entre `$$` ou `\[ ... \]`.
* 📊 Tu peux ajouter des **captions** (`> Citation`) pour des remarques ou des rappels.
* 🧠 Sauvegarde régulièrement (Ctrl + S).

# :books: References

|  | 2 Variables |
|--------------------------------------|----------------------------------------------------------------|
| Ensemble (set) | ${\displaystyle \{(k,x)\ \|\ k\in K\wedge x\in X\wedge P(x)\}}$ [^1] |

[^1]: https://en.wikipedia.org/wiki/Set-builder_notation

```bash
jupyter nbconvert --to markdown MON_NOTEBOOK.ipynb
```
