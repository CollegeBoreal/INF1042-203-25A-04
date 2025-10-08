


```mermaid
flowchart TD
A([Début]) --> B[/Lire A, B/]
B --> C{A > B ?}
C -- Oui --> D[Afficher "A est le plus grand"]
C -- Non --> E[Afficher "B est le plus grand"]
D --> F([Fin])
E --> F([Fin])
