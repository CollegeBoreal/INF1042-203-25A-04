
'''mermaid
flowchart TD
    A([Début]) --> B[/Lire N/]
    B --> C[Initialiser S ← 0, i ← 1]
    C --> D{i ≤ N ?}
    D -- Oui --> E[S ← S + i]
    E --> F[i ← i + 1]
    F --> D
    D -- Non --> G[Afficher S]
    G --> H([Fin])


