
flowchart TD
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:1.5px
    style C fill:#bfb,stroke:#333,stroke-width:1.5px
    style D fill:#ffb,stroke:#333,stroke-width:1.5px
    style E fill:#bfb,stroke:#333,stroke-width:1.5px
    style F fill:#bfb,stroke:#333,stroke-width:1.5px
    style G fill:#f9f,stroke:#333,stroke-width:2px

    A([Début]) --> B[/Lire N/]
    B --> C[Calculer reste = N mod 2]
    C --> D{reste == 0 ?}
    D -- Oui --> E[Afficher "N est pair"]
    D -- Non --> F[Afficher "N est impair"]
    E --> G([Fin])
    F --> G([Fin])

