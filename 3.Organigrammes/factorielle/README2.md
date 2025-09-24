Parfait ! Voici une **version ultra-visuelle et pédagogique** du calcul de la factorielle (itératif et récursif) avec **Mermaid**, utilisant **couleurs, styles et formes**. Cette version est prête pour GitHub Markdown.

---

# **Factorielle – Version visuelle avec couleurs Mermaid**

## 1️⃣ Itératif (Boucle)

```mermaid
flowchart TD
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:1.5px
    style C fill:#bfb,stroke:#333,stroke-width:1.5px
    style D fill:#ffb,stroke:#333,stroke-width:1.5px
    style E fill:#ffb,stroke:#333,stroke-width:1.5px
    style F fill:#bfb,stroke:#333,stroke-width:1.5px
    style G fill:#bbf,stroke:#333,stroke-width:2px
    style H fill:#f9f,stroke:#333,stroke-width:2px

    A([Début]) --> B[/Lire N/]
    B --> C[Initialiser factor = 1, i = 1]
    C --> D{i <= N ?}
    D -- Oui --> E[factor = factor * i]
    E --> F[i = i + 1]
    F --> D
    D -- Non --> G[Écrire factor]
    G --> H([Fin])
```

**Couleurs :**

* Violet clair → début/fin
* Bleu → lecture / sortie
* Vert → instructions
* Jaune → conditions

---

## 2️⃣ Récursif

```mermaid
flowchart TD
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:1.5px
    style C fill:#bfb,stroke:#333,stroke-width:1.5px
    style D fill:#ffb,stroke:#333,stroke-width:1.5px
    style E fill:#bfb,stroke:#333,stroke-width:1.5px
    style F fill:#bfb,stroke:#333,stroke-width:1.5px
    style G fill:#bbf,stroke:#333,stroke-width:1.5px
    style H fill:#bfb,stroke:#333,stroke-width:1.5px
    style I fill:#f9f,stroke:#333,stroke-width:2px

    A([Debut]) --> B[/Lire N/]
    B --> C[Appeler fonction factorielle N]
    C --> D{N <= 1 ?}
    D -- Oui --> E[Retourner 1]
    D -- Non --> F[Appeler fonction factorielle N-1]
    F --> G[Retourner N multiplie factorielle N-1]
    E --> H[Afficher resultat]
    G --> H
    H --> I([Fin])
```

**Couleurs :**

* Violet → début/fin
* Bleu → lecture / sortie
* Vert → instructions / retours de fonction
* Jaune → conditions

---

## 3️⃣ Bonus : Styles Mermaid avancés

* Tu peux utiliser des **formes différentes** pour chaque type d’action :

  * `shape: manual-input` pour l’entrée
  * `shape: procs` pour les instructions
  * `shape: diamond` pour les conditions
  * `shape: manual-file` pour début/fin

Exemple itératif stylé :

```mermaid
flowchart TD
    A@{shape: manual-file, label:"Début"} --> B@{shape: manual-input, label:"Lire N"}
    B --> C@{shape: procs, label:"factor = 1, i = 1"}
    C --> D@{shape: diamond, label:"i <= N ?"}
    D -- Oui --> E@{shape: procs, label:"factor = factor * i"}
    E --> F@{shape: procs, label:"i = i + 1"}
    F --> D
    D -- Non --> G@{shape: procs, label:"Écrire factor"}
    G --> H@{shape: manual-file, label:"Fin"}
```

---

💡 **Résultat :**
Ces versions sont **colorées, structurées et pédagogiques**, parfaites pour :

* GitHub Markdown
* Présentations
* Cours et tutoriels interactifs
