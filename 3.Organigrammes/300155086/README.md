



flowchart TD
    B@{ shape: manual-input, label: "Lire N"}
    C@{ shape: procs, label: "Appeler factorielle(N)"}
    D@{ shape: diamond, label: "N <= 1 ?"}
    E@{ shape: procs, label: "Retourner 1"}
    F@{ shape: procs, label: "factorielle(N-1)"}
    G@{ shape: procs, label: "Retourner N * factorielle(N-1)"}
    H@{ shape: procs, label: "Afficher résultat"}

    A([Debut]) --> B
    B --> C
    C --> D
    D -- Oui --> E
    D -- Non --> F
    F --> G
    E --> H
    G --> H
    H --> I([Fin])


