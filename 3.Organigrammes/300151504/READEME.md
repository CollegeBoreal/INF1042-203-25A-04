flowchart TD

    A([Début]) --> B[Lire un nombre]
    B --> C{nombre > 0 ?}
    C -->|Oui| D[Afficher "Positif"]
    C -->|Non| E[Afficher "Négatif"]
    D --> F([Fin])
    E --> F([Fin])

