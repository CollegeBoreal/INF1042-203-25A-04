# Organigramme : Vérifier si un nombre est pair ou impair

```mermaid
flowchart TD
    A([Début]) --> B[Entrer un nombre]
    B --> C{Le nombre est-il pair ?}
    C -->|Oui| D[Afficher le nombre est pair]
    C -->|Non| E[Afficher le nombre est impair]
    D --> F([Fin])
    E --> F
