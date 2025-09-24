    
```mermaid
    graph TD
        A[Départ] --> B{Une décision ?};
        B -->|Oui| C[Action 1];
        B -->|Non| D[Action 2];
        C --> E[Fin];
        D --> E[Fin];
