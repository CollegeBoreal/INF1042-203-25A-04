```mermaid
flowchart TD
    A([Début]) --> B[Lire la proposition mathématique]
    B --> C{Est-elle vraie ?}
    C -->|Oui| D[Conclusion : Proposition vérifiée]
    C -->|Non| E[Conclusion : Proposition fausse]
    D --> F([Fin])
    E --> F([Fin])
