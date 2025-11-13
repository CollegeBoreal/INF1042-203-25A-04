```mermaid
flowchart TD
    A[Début] --> B[Lire la valeur de x]
    B --> C{La proposition est-elle donnée ?}
    C -->|Non| Z[Afficher 'Erreur : proposition manquante'] --> F[Fin]
    C -->|Oui| D{La condition est-elle vraie ?}
    D -->|Oui| E[Afficher 'Proposition vérifiée']
    D -->|Non| G[Afficher 'Proposition fausse']
    E --> F[Fin]
    G --> F
