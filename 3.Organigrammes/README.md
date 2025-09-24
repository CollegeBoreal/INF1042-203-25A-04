# 3.Organigrammes

[:tada: Participation](.scripts/Participation.md)

## :a: Examples

:bulb: **Flowchart** en Anglais

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
