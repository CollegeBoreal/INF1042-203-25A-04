<<<<<<< HEAD
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
=======
# Organigramme : Vérifier si un nombre est pair ou impair

```mermaid
flowchart TD
    A([Début]) --> B[Entrer un nombre]
    B --> C{Le nombre est-il pair ?}
    C -->|Oui| D[Afficher le nombre est pair]
    C -->|Non| E[Afficher le nombre est impair]
    D --> F([Fin])
    E --> F
>>>>>>> e1d50e24795f641c3609493c501757d054c199a0
