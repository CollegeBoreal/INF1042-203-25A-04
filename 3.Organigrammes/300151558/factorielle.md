mermaid

flowchart TD



A(\[Début]) --> B\[Lire N]

B --> C{N < 0 ?}



C -->|Oui| Z\[Afficher "Erreur"]

Z --> I(\[Fin])



C -->|Non| D\[Initialiser factor = 1 et i = 1]



D --> E{i <= N ?}



E -->|Oui| F\[factor = factor \* i]

F --> G\[i = i + 1]

G --> E



E -->|Non| H\[Afficher factor]

H --> I(\[Fin])



