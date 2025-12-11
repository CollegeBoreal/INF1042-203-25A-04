```mermaid
flowchart TD
    A([Début]) --> B[/Lire N/]
    B --> C[Appeler fonction factorielle]
    C --> D{N ≤ 1 ?}
    D -->|Oui| E[Retourner 1]
    D -->|Non| F[Retourner N * factorielle(N-1)]
    E --> G[Afficher résultat]
    F --> G
    G --> H((Fin))
```

