# main.py
"""
Script principal qui importe le module convertisseur et teste f(x)
"""

from embellisseur import f

print("=== Démonstration de f(x) avec @singledispatch ===\n")

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

from convertisseur import convert_all

print("=== convertir une liste ===\n")

# Exemple : convertir une liste
tests = {
    "binaire": 8,
    "hexadécimal": 255,
    "int": "42",
    "float": "3.14",
    "str": 123,
    "list": (1, 2, 3),
    "tuple": [1, 2, 3],
    "array": [4, 5, 6],
    "dict": [("a", 1), ("b", 2)]
}

for t, val in tests.items():
    print(f"\n{t.upper()} : {val}")
    for name, result in convert_all(val):
        if name == t:
            print(f"→ {result}")

