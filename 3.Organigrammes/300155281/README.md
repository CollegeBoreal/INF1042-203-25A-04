
    ORGANIGRAMME QUI DEFINIT LA PARITE D UN NOMBRE
```mermaid
    graph TD
       debut[Début] --> A[Entrer un nombre];
        A --> B{Nombre % 2 == 0 ?};
        B -->|Oui| C[Le nombre est pair];
        B -->|Non| D[Le nombre est impair];
        C & D--> fin[Fin]

    ORGANIGRAMME QUI ADDITIONNE 2 NOMBRES

```mermaid
    graph TD
        debut[debut] --> A[entrer le premier nombre];
        A -->B[entrer le deuxieme nombre];
        B -->C[calculer la somme= premier nombre+deuxieme nombre];
        C -->D[ Afficher la somme ];
        D -->fin[fin];
        
    
