
```mermaid
flowchart TD
  start((Debut))
  input[/Entrer n/]
  callFibo([Appeler Fibo(n)])
  display([Afficher le resultat])
  end((Fin))

  start --> input --> callFibo --> display --> end

  subgraph Fibo_Function [Fonction Fibo(n)]
    A{n <= 1 ?}
    A -- Oui --> R1([Retourner n])
    A -- Non --> C1([x = Fibo(n - 1)])
    C1 --> C2([y = Fibo(n - 2)])
    C2 --> R2([Retourner x + y])
  end

  callFibo --> A
```
