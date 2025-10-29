# 🐍 Les variables en Python

[:tada: Participation](.scripts/Participation.md)

---

## 🎯 Qu’est-ce qu’une variable ?

Une **variable** est un **nom symbolique** qui fait référence à une **valeur stockée en mémoire**.
Elle permet de **stocker**, **manipuler** et **réutiliser** des données dans un programme.

```python
nom = "Alice"
age = 25
```

Ici :

* `nom` pointe vers la valeur `"Alice"`
* `age` pointe vers la valeur `25`

---

## 🧠 Les types de variables simples

Chaque valeur en Python a un **type**, c’est-à-dire une **catégorie de données**.
Python détermine automatiquement le type selon la valeur donnée.

| Exemple            | Type    | Description             |
| ------------------ | ------- | ----------------------- |
| `10`               | `int`   | Entier                  |
| `3.14`             | `float` | Nombre décimal          |
| `"Bonjour"`        | `str`   | Chaîne de caractères    |
| `True`             | `bool`  | Booléen                 |
| `[1, 2, 3]`        | `list`  | Liste modifiable        |
| `(1, 2, 3)`        | `tuple` | Liste non modifiable    |
| `{"nom": "Alice"}` | `dict`  | Dictionnaire clé/valeur |

💡 Pour connaître le type d’une variable :

```python
x = 42
print(type(x))  # <class 'int'>
```

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

# :a: Types de variables en Python :snake:

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

### :rocket: Copier le fichier `RAPPORT.ipynb`

- [ ] Se diriger vers le répertoire avec :id: (votre identifiant boreal)
   - [ ] `cd ` :id:
- [ ] Copier le fichier `RAPPORT.ipynb`

```sh
cp ../.lib/RAPPORT.ipynb .
```

### 🔄 Exercices

- [ ] Démarrer `jupyter` dans son répertoire :id:
- [ ] Modifier les exemples de variables et mettre à son goût

