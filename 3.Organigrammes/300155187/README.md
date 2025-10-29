
```mermaid
flowchart TD
    A[Start] --> B[Dividend = 12.5]
    B --> C[Divisor = 2.5]
    C --> D[Compute Quotient = 12.5 / 2.5]
    D --> E[Quotient = 5.0]
    E --> F[End]

```mermaid
flowchart TD
    A([Début]) --> B[Initialiser A = 255, B = 3]
    B --> C{B = 0 ?}
    C -->|Oui| D[/"Erreur : division par zéro"/]
    D --> C
    C -->|Non| E[Calculer Quotient = A // B]
    E --> F[Calculer Reste = A mod B]
    F --> G{Reste = 0 ?}
    G -->|Oui| H[/Afficher "255 ÷ 3 = 85, division exacte"/]
    G -->|Non| I[/Afficher "255 ÷ 3 = 85, reste 0"/]
    H --> J([Fin])







