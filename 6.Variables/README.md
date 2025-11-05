# 🐍 Leçon : Les variables en Python

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

