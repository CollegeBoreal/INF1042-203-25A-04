# :abacus:  organigramme de factorielle d'un nombre
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
  

