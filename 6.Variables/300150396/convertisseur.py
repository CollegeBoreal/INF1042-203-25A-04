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

from moyenne import algebrique, geometrique

print("La moyenne algébrique est :", algebrique([2, 4.5, 6, 8, 10]))
print("La moyenne géométrique est :", geometrique([2, 4.5, 6, 8, 10]))

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

## 🧠 Conclusion

Ce rapport montre comment :
- Une même fonction (`f`) peut traiter plusieurs types de données.
- Des fonctions mathématiques (`algebrique`, `geometrique`) peuvent être réutilisées.
- Les **ensembles** et **comprehensions** facilitent les filtres et combinaisons de données.

> 🧩 Python est un langage à typage dynamique, où les fonctions peuvent être générales,
> et les structures (listes, tuples, sets, dictionnaires) très expressives.