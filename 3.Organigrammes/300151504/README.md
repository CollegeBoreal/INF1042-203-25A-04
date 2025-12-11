graph TD
    A([Début]) --> B[Lire un nombre]
    B --> C{Le nombre est-il pair ?}
    C -->|Oui| D[Afficher "Pair"]
    C -->|Non| E[Afficher "Impair"]
    D --> F([Fin])
    E --> F([Fin])

