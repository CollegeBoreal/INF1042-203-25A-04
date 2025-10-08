```mermaid
flowchart TD
    A[Start] --> B[Enter Dividend]
    B --> C[Enter Divisor]
    C --> D{Is Divisor = 0?}
    D -- Yes --> E[Error: Division by zero]
    D -- No --> F[Compute Quotient = Dividend / Divisor]
    F --> G[Display Result]
    G --> H[End]








