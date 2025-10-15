```mermaid

flowchart TD

&nbsp;   A(\[Début]) --> B\[/Lire N/]

&nbsp;   B --> C\[Initialiser somme = 0 et i = 1]

&nbsp;   C --> D{i <= N ?}

&nbsp;   D -- Oui --> E\[somme = somme + i]

&nbsp;   E --> F\[i = i + 1]

&nbsp;   F --> D

&nbsp;   D -- Non --> G\[Écrire somme]

&nbsp;   G --> H(\[Fin])

