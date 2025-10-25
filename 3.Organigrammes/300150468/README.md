flowchart TD
    A@{ shape: manual-file, label: "Début du programme"}
    B@{ shape: manual-input, label: "Lire N"}
    C@{ shape: procs, label: "Initialiser factor = 1, i = 1"}
    D@{ shape: diamond, label: "i <= N ?"}
    E@{ shape: procs, label: "factor = factor * i"}
    F@{ shape: procs, label: "i = i + 1"}
    G@{ shape: procs, label: "Écrire factor"}
    H@{ shape: manual-file, label: "Fin du programme"}

    A --> B
    B --> C
    C --> D
    D -- Oui --> E
    E --> F
    F --> D
    D -- Non --> G
    G --> H
