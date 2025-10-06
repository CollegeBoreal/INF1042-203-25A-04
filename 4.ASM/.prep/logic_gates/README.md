Here’s a handy list of the **most common logic gates in French**, with their English equivalents:

| English        | French                | Symbol / Notes     |
| -------------- | --------------------- | ------------------ |
| AND            | porte ET              | A ⋅ B or A ∧ B     |
| OR             | porte OU              | A + B or A ∨ B     |
| NOT / Inverter | porte NON             | ¬A or A̅           |
| NAND           | porte NON-ET          | ¬(A ⋅ B)           |
| NOR            | porte NON-OU          | ¬(A + B)           |
| XOR            | porte OU exclusif     | A ⊕ B              |
| XNOR           | porte NON-OU exclusif | ¬(A ⊕ B)           |
| BUFFER         | tampon                | just passes signal |

💡 **Tip:** In French textbooks, “porte” = “gate,” and the rest describes the operation.

```mermaid
graph TD
    LUT[LUT / Bloc Logique] --> ET[Porte ET]
    LUT --> OU[Porte OU]
    LUT --> NON[Porte NON]
    LUT --> NAND[Porte NON-ET]
    LUT --> NOR[Porte NON-OU]
    LUT --> XOR[Porte OU Exclusif]
    LUT --> XNOR[Porte NON-OU Exclusif]
    LUT --> TAM[Buffer / Tampon]
```


```mermaid
graph LR
    A([A]) --> G{{AND}}
    B([B]) --> G{{AND}}
    G --> F([F])
```

```mermaid
graph TD
    %% Entrées
    A([A])
    B([B])
    F([F = A·B])
    Vdd((Vdd))
    GND((GND))

    %% Transistors PMOS (pull-up)
    P1[PMOS P1]
    P2[PMOS P2]

    %% Transistors NMOS (pull-down)
    N1[NMOS N1]
    N2[NMOS N2]

    %% Connexions PMOS (en parallèle)
    Vdd --> P1
    Vdd --> P2
    A -->|gate| P1
    B -->|gate| P2
    P1 --> F
    P2 --> F

    %% Connexions NMOS (en série)
    F --> N1
    N1 --> N2
    N2 --> GND
    A -->|gate| N1
    B -->|gate| N2
```
