# types_demo.py
# Démonstration de fonctions Python pour différents types de données

from array import array
from typing import Any, List, Tuple

# --- Fonctions de conversion simples --- #

def to_binary(x: int) -> str:
    """Retourne la représentation binaire de x (préfixée par 0b)."""
    return bin(x)

def to_hex(x: int) -> str:
    """Retourne la représentation hexadécimale de x (préfixée par 0x)."""
    return hex(x)

def to_int(x) -> int:
    """Convertit x en entier."""
    return int(x)

def to_float(x) -> float:
    """Convertit x en nombre à virgule flottante."""
    return float(x)

def to_str(x) -> str:
    """Convertit x en chaîne de caractères."""
    return str(x)

def to_list(x) -> list:
    """Convertit x en liste (si possible)."""
    return list(x)

def to_tuple(x) -> tuple:
    """Convertit x en tuple (si possible)."""
    return tuple(x)

def to_array(x) -> array:
    """Convertit une séquence numérique en tableau du module array."""
    return array('i', x)

def to_dict(x) -> dict:
    """Convertit une liste de paires ou un dictionnaire existant."""
    return dict(x)

# --- Fonction principale pour tester toutes les conversions --- #

def convert_all(x) -> List[Tuple[str, Any]]:
    """
    Retourne une liste contenant toutes les représentations de x
    selon les fonctions définies ci-dessus.
    """
    results = []

    try:
        results.append(("binaire", to_binary(int(x))))
    except Exception as e:
        results.append(("binaire", f"Erreur: {e}"))

    try:
        results.append(("hexadécimal", to_hex(int(x))))
    except Exception as e:
        results.append(("hexadécimal", f"Erreur: {e}"))

    try:
        results.append(("int", to_int(x)))
    except Exception as e:
        results.append(("int", f"Erreur: {e}"))

    try:
        results.append(("float", to_float(x)))
    except Exception as e:
        results.append(("float", f"Erreur: {e}"))

    try:
        results.append(("str", to_str(x)))
    except Exception as e:
        results.append(("str", f"Erreur: {e}"))

    try:
        results.append(("list", to_list(x)))
    except Exception as e:
        results.append(("list", f"Erreur: {e}"))

    try:
        results.append(("tuple", to_tuple(x)))
    except Exception as e:
        results.append(("tuple", f"Erreur: {e}"))

    try:
        results.append(("array", to_array(x)))
    except Exception as e:
        results.append(("array", f"Erreur: {e}"))

    try:
        results.append(("dict", to_dict(x)))
    except Exception as e:
        results.append(("dict", f"Erreur: {e}"))

    return results


# --- Exemple d'utilisation --- #
if __name__ == "__main__":
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

