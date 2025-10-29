# Types de variables de base en Python :snake:

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


