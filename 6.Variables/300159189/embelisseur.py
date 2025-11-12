# convertisseur.py
"""
Module de démonstration : fonction f(x) avec @singledispatch
gérant plusieurs types (int, float, str, list, tuple, dict)
"""

from functools import singledispatch
from array import array

# --- Fonction principale avec @singledispatch --- #
@singledispatch
def f(x) -> dict:
    """Fonction générique pour tous les types non enregistrés."""
    return f"Type non supporté : {type(x).__name__}"

# --- int --- #
@f.register
def _(x: int) -> dict:
    return {
        "binaire": bin(x),
        "hexadécimal": hex(x),
        "int": x,
        "float": float(x),
        "str": str(x)
    }

# --- float --- #
@f.register
def _(x: float) -> dict:
    return {
        "float": x,
        "int": int(x),
        "str": str(x)
    }

# --- str --- #
@f.register
def _(x: str) -> dict:
    return {
        "str": x,
        "list": list(x),
        "tuple": tuple(x)
    }

# --- list --- #
@f.register
def _(x: list) -> dict:
    numeric_items = [i for i in x if isinstance(i, (int, float))]
    return {
        "list": x,
        "tuple": tuple(x),
        "array": array('i', numeric_items) if numeric_items else None,
        "str": str(x)
    }

# --- tuple --- #
@f.register
def _(x: tuple) -> dict:
    numeric_items = [i for i in x if isinstance(i, (int, float))]
    return {
        "tuple": x,
        "list": list(x),
        "array": array('i', numeric_items) if numeric_items else None,
        "str": str(x)
    }

# --- dict --- #
@f.register
def _(x: dict) -> dict:
    return {
        "dict": x,
        "list_clés": list(x.keys()),
        "list_valeurs": list(x.values()),
        "str": str(x)
    }

# --- Test direct --- #
if __name__ == "__main__":
    exemples = [
        42,
        3.14,
        "abc",
        [1, 2, 3],
        (4, 5, 6),
        {"a": 1, "b": 2}
    ]

    for e in exemples:
        print(f"\n--- f({e}) ---")
        for k, v in f(e).items():
            print(f"{k:12} -> {v}")


