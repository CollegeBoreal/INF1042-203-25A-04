# 🐍 Leçon : Les variables en Python

[:tada: Participation](.scripts/Participation.md)

---

## 🎯 Qu’est-ce qu’une variable ?

Une **variable** est un **nom** qui sert à **stocker une valeur** dans la mémoire de l’ordinateur.
Elle permet de **réutiliser** et **modifier** ces valeurs plus tard dans le programme.

👉 On peut imaginer une variable comme une **boîte étiquetée** contenant une valeur.

```python
nom = "Alice"
age = 25
```

Ici :

* `nom` contient la chaîne `"Alice"`
* `age` contient l’entier `25`

---

## 🧠 Règles pour nommer une variable

* Le nom **doit commencer** par une lettre ou un `_` (underscore)
* Il **ne peut pas commencer** par un chiffre
* Il **ne contient pas d’espace**
* Il est **sensible à la casse** (`Age` ≠ `age`)

✅ Correct :

```python
prenom = "Bob"
_age = 30
```

❌ Incorrect :

```python
2age = 25    # Commence par un chiffre
mon nom = "Eve"  # Espace interdit
```

---

## 🔢 Types de valeurs possibles

Python détecte automatiquement le **type de la valeur** :

```python
x = 10          # int (entier)
y = 3.14        # float (décimal)
nom = "Boréal"  # str (chaîne de caractères)
vrai = True     # bool (booléen)
```

Pour vérifier le type :

```python
print(type(x))  # <class 'int'>
```

---

## 🔁 Modifier une variable

Une variable peut être **réaffectée** :

```python
note = 80
note = note + 5
print(note)  # 85
```

---

## 📦 Affectation multiple

Python permet d’assigner plusieurs variables en une ligne :

```python
a, b, c = 1, 2, 3
```

---

## 🧹 Supprimer une variable

Pour supprimer une variable :

```python
del a
```

---

### 💡 En résumé

| Élément      | Exemple              | Type    |
| ------------ | -------------------- | ------- |
| Entier       | `x = 10`             | `int`   |
| Décimal      | `x = 3.14`           | `float` |
| Texte        | `x = "Bonjour"`      | `str`   |
| Booléen      | `x = True`           | `bool`  |
| Liste        | `x = [1,2,3]`        | `list`  |
| Dictionnaire | `x = {"nom": "Bob"}` | `dict`  |

---

## 🧩 **Types de base**

| Type      | Exemple      | Description                          |
| --------- | ------------ | ------------------------------------ |
| `int`     | `x = 42`     | Entier (positif ou négatif)          |
| `float`   | `x = 3.14`   | Nombre à virgule flottante           |
| `complex` | `x = 2 + 3j` | Nombre complexe                      |
| `bool`    | `x = True`   | Valeur booléenne (`True` ou `False`) |
| `str`     | `"Bonjour"`  | Chaîne de caractères                 |

---

## 📦 **Types de collections**

| Type        | Exemple                       | Description                       |
| ----------- | ----------------------------- | --------------------------------- |
| `list`      | `[1, 2, 3]`                   | Liste ordonnée et modifiable      |
| `tuple`     | `(1, 2, 3)`                   | Liste ordonnée **non modifiable** |
| `set`       | `{1, 2, 3}`                   | Ensemble **unique**, non ordonné  |
| `frozenset` | `frozenset({1, 2, 3})`        | Ensemble **non modifiable**       |
| `dict`      | `{"nom": "Alice", "âge": 25}` | Dictionnaire clé-valeur           |

---

## ⚙️ **Types spéciaux**

| Type         | Exemple                   | Description                          |
| ------------ | ------------------------- | ------------------------------------ |
| `NoneType`   | `x = None`                | Valeur vide ou absence de valeur     |
| `bytes`      | `b"Bonjour"`              | Suite d’octets immuable              |
| `bytearray`  | `bytearray([65, 66, 67])` | Suite d’octets modifiable            |
| `memoryview` | `memoryview(b"Hello")`    | Vue mémoire sur des données binaires |
| `range`      | `range(5)`                | Séquence d’entiers itérables         |
| `array`      | `array('i', [1,2,3])`     | Tableau typé (module `array`)        |

---

## 🔬 **Types avancés (objets)**

| Type               | Exemple                   | Description          |
| ------------------ | ------------------------- | -------------------- |
| `function`         | `def f(): pass`           | Fonction Python      |
| `module`           | `import math`             | Module chargé        |
| `class` / `object` | `class Voiture: pass`     | Classe et instance   |
| `iterator`         | `iter([1,2,3])`           | Objet itérable       |
| `generator`        | `(x*x for x in range(5))` | Générateur paresseux |

---

## 🔄 Mutabilité et immutabilité

C’est une **notion essentielle** 🧩 :
Elle détermine si une **valeur peut être modifiée** sans changer son **identité en mémoire**.

### 🔸 **Objets immuables**

Ce sont des objets **dont la valeur ne peut pas être modifiée** après leur création.
Chaque modification crée **un nouvel objet** en mémoire.

Exemples : `int`, `float`, `str`, `tuple`, `bool`

```python
x = 10
print(id(x))  # adresse mémoire
x = x + 1
print(id(x))  # nouvelle adresse → nouvel objet
```

➡️ Le `int` est immuable : chaque opération crée une nouvelle valeur.

---

### 🔹 **Objets muables**

Ces objets peuvent être **modifiés directement** en mémoire (leur adresse ne change pas).

Exemples : `list`, `dict`, `set`

```python
liste = [1, 2, 3]
print(id(liste))
liste.append(4)
print(id(liste))  # même adresse → objet modifié
```

➡️ La `list` est muable : on peut modifier son contenu sans créer un nouvel objet.

---

## 🧩 Illustration complète

| Type    | Exemple          | Muable ? |
| ------- | ---------------- | -------- |
| `int`   | `x = 5`          | ❌ Non    |
| `float` | `x = 3.14`       | ❌ Non    |
| `str`   | `x = "Salut"`    | ❌ Non    |
| `tuple` | `(1, 2)`         | ❌ Non    |
| `list`  | `[1, 2, 3]`      | ✅ Oui    |
| `dict`  | `{"nom": "Eve"}` | ✅ Oui    |
| `set`   | `{1, 2, 3}`      | ✅ Oui    |

---

## ⚙️ En résumé

* 🔹 **Variable** → nom qui référence une valeur
* 🔹 **Type** → nature de la donnée (entier, texte, liste, etc.)
* 🔹 **Immuable** → valeur fixe, nouvelle copie lors des modifications
* 🔹 **Muable** → peut être modifiée directement


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

##### 🟦 Cellule Markdown (titre principal)

```markdown
# 🪐 RAPPORT : Analyse de Code Python (Variables, Moyennes, Ensembles)

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
