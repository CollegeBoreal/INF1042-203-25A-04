```mermaid
flowchart TD
    A[Début] --> B[Entrer un nombre N]
    B --> C{N < 2 ?}
    C -- Oui --> D[N n'est pas premier]
    C -- Non --> E[i = 2]
    E --> F{i ≤ √N ?}
    F -- Non --> G[N est premier]
    F -- Oui --> H{N mod i = 0 ?}
    H -- Oui --> D
    H -- Non --> I[i = i + 1]
    I --> F
    D --> J[Fin]
    G --> J
