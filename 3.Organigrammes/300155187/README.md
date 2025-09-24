```mermaid
flowchart TD
    A[Démarrage] --> B[Lire capteurs<br/>(caméra, lidar, GPS)]
    B --> C[Localiser le véhicule<br/>(filtre de Kalman, SLAM)]
    C --> D[Détecter obstacles & routes]
    D --> E{But atteint ?}
    E -- Non --> F[Planification globale<br/>(A*, Dijkstra)]
    F --> G[Planification locale<br/>(éviter obstacles)]
    G --> H[Contrôle mouvement<br/>(Pure Pursuit, PID)]
    H --> I[Envoyer commandes<br/>(moteur, direction, frein)]
    I --> B
    E -- Oui --> J[Arrêt du véhicule]
