```mermaid
flowchart TD
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:1.5px
    style C fill:#bfb,stroke:#333,stroke-width:1.5px
    style D fill:#ffb,stroke:#333,stroke-width:1.5px
    style E fill:#bfb,stroke:#333,stroke-width:1.5px
    style F fill:#bfb,stroke:#333,stroke-width:1.5px
    style G fill:#f9f,stroke:#333,stroke-width:2px

    A([Début]) --> B[/Lire N/]
    B --> C[Initialiser somme = 0, i = 1]
    C --> D{i ≤ N ?}
    D -- Oui --> E[somme = somme + i \n i = i + 1]
    E --> D
    D -- Non --> F[Afficher somme]
    F --> G([Fin])


