# cet organigramme permet de determiner la parité d'un nombre
    
```mermaid
    graph TD
       debut[Début] --> A[Entrer un nombre];
        A --> B{Nombre % 2 == 0 ?};
        B -->|Oui| C[Le nombre est pair];
        B -->|Non| D[Le nombre est impair];
        C & D--> fin[Fin]

    


   
