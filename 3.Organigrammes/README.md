
```mermaid
flowchart RL
    A@{ shape: manual-file, label: "File Handling"}
    B@{ shape: manual-input, label: "User Input"}
    C@{ shape: docs, label: "Multiple Documents"}
    D@{ shape: procs, label: "Process Automation"}
    E@{ shape: paper-tape, label: "Paper Records"}
```

```mermaid
flowchart TD
    A([Début]) --> B[/Lire N/]
    B --> C{N % 2 == 0 ?}
    C -- Oui --> D[Écrire "Pair"]
    C -- Non --> E[Écrire "Impair"]
    D --> F([Fin])
    E --> F([Fin])
```
