# 3.Organigrammes

[:tada: Participation](.scripts/Participation.md)

## :o: Definition

En programmation, un organigramme (ou **flowchart**) sert à représenter visuellement la logique d’un algorithme, avec des symboles standards :

- Ovales : début / fin
- Rectangles : actions ou instructions
- Losanges : conditions (oui / non)
- Flèches : enchaînement

## :a: Examples

- [ ] La somme d'un chiffre `N`

```mermaid
flowchart TD
    A([Début]) --> B[/Lire N/]
    B --> C[Initialiser somme = 0 et i = 1]
    C --> D{i <= N ?}
    D -- Oui --> E[somme = somme + i]
    E --> F[i = i + 1]
    F --> D
    D -- Non --> G[Écrire somme]
    G --> H([Fin])
```

- [ ] Un organigramme fonctionnel

```mermaid
flowchart RL
    A@{ shape: manual-file, label: "File Handling"}
    B@{ shape: manual-input, label: "User Input"}
    C@{ shape: docs, label: "Multiple Documents"}
    D@{ shape: procs, label: "Process Automation"}
    E@{ shape: paper-tape, label: "Paper Records"}
```

- [ ] Un organigramme expliquant la fonction paire

```mermaid
flowchart TD
    A([Début]) --> B[/Lire N/]
    B --> C{N % 2 == 0 ?}
    C -- Oui --> D[Écrire Pair]
    C -- Non --> E[Écrire Impair]
    D --> F([Fin])
    E --> F([Fin])
```
## :abacus: factorielle

### **Leçon : Calcul de la factorielle avec organigrammes**

### 1️⃣ Définition de la factorielle

La **factorielle** d’un nombre entier positif `N` (notée `N!`) est le produit de tous les entiers positifs de 1 à `N` :

$$
N! = 1 × 2 × 3 × … × N
$$

Cas particuliers :

* `0! = 1`
* `1! = 1`

La factorielle est utilisée en mathématiques, statistiques et programmation (permutations, combinaisons, etc.).

---

### 2️⃣ Algorithme itératif

#### Étapes :

1. Lire un nombre `N`.
2. Initialiser `factor = 1`.
3. Pour `i` de 1 à `N` : multiplier `factor` par `i`.
4. Afficher `factor`.

---

#### 2.1 Organigramme Mermaid classique

```mermaid
flowchart TD
    A([Début]) --> B[/Lire N/]
    B --> C[Initialiser factor = 1 et i = 1]
    C --> D{i <= N ?}
    D -- Oui --> E[factor = factor * i]
    E --> F[i = i + 1]
    F --> D
    D -- Non --> G[Écrire factor]
    G --> H([Fin])
```

---

#### 2.2 Organigramme avec **shapes personnalisés**

```mermaid
flowchart TD
    B@{ shape: manual-input, label: "Lire N"}
    C@{ shape: procs, label: "Initialiser factor = 1, i = 1"}
    D@{ shape: diamond, label: "i <= N ?"}
    E@{ shape: procs, label: "factor = factor * i"}
    F@{ shape: procs, label: "i = i + 1"}
    G@{ shape: procs, label: "Écrire factor"}

    A([Début]) --> B
    B --> C
    C --> D
    D -- Oui --> E
    E --> F
    F --> D
    D -- Non --> G
    G --> H([Fin])
```

---

### 3️⃣ Algorithme récursif

#### Étapes :

1. Fonction `factorielle(n)` :

   * Si `n <= 1` → retourner 1
   * Sinon → retourner `n * factorielle(n-1)`
2. Lire `N`
3. Appeler `factorielle(N)`
4. Afficher le résultat

---

#### 3.1 Organigramme Mermaid classique (récursion)

```mermaid
flowchart TD
    A([Debut]) --> B[/Lire N/]
    B --> C[Appeler factorielle N]
    C --> D{N <= 1 ?}
    D -- Oui --> E[Retourner 1]
    D -- Non --> F[Appeler factorielle N-1]
    F --> G[Retourner N * factorielle N-1]
    E --> H[Afficher resultat]
    G --> H
    H --> I([Fin])
```
---

#### 3.2 Organigramme avec **shapes personnalisés**

Example de récursion

```mermaid
flowchart TD
    B@{ shape: manual-input, label: "Lire N"}
    C@{ shape: procs, label: "Appeler factorielle(N)"}
    D@{ shape: diamond, label: "N <= 1 ?"}
    E@{ shape: procs, label: "Retourner 1"}
    F@{ shape: procs, label: "factorielle(N-1)"}
    G@{ shape: procs, label: "Retourner N * factorielle(N-1)"}
    H@{ shape: procs, label: "Afficher résultat"}

    A([Debut]) --> B
    B --> C
    C --> D
    D -- Oui --> E
    D -- Non --> F
    F --> G
    E --> H
    G --> H
    H --> I([Fin])
```

---

### 4️⃣ Bonnes pratiques pour les organigrammes

1. Toujours **commencer par Début** et finir par **Fin**.
2. Utiliser des **formes cohérentes** pour les mêmes types d’actions.
3. Garder le diagramme **simple et lisible**, éviter les croisements de flèches.
4. Mettre des **étiquettes claires** sur les flèches pour les conditions (Oui / Non).
5. Vérifier la logique en parallèle du code.

# :books: References

- [ ] [:mermaid: Mermaid](https://mermaid.js.org)
