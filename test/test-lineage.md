```Mermaid
graph TD
    %% Source Data
    A[Raw Sales Data] --> B[Data Warehouse]
    C[Customer Database] --> B
    D[Product Catalog] --> B
    
    %% Staging Area
    B --> E[Staging Layer]
    E --> F[Data Processing]
    
    %% Transformation Nodes
    F --> G[Sales Aggregation]
    F --> H[Customer Segmentation]
    F --> I[Product Analytics]
    
    %% Business Intelligence
    G --> J[Sales Dashboard]
    H --> K[Customer Insights]
    I --> L[Product Reports]
    
    %% Data Quality Checks
    B --> M[Data Validation]
    M --> N[Quality Reports]
    
    %% Metadata
    O[Metadata Store] --> P[Lineage Tracking]
    P --> B
    
    %% Styling
    classDef source fill:#e1f5fe,stroke:#000;
    classDef staging fill:#fff3e0,stroke:#000;
    classDef transformation fill:#e8f5e9,stroke:#000;
    classDef output fill:#fce4ec,stroke:#000;
    classDef metadata fill:#f3e5f5,stroke:#000;
    
    class A,C,D source
    class B,E staging
    class F,G,H,I transformation
    class J,K,L, output
    class M,N metadata
    class O,P metadata
    
    %% Arrows
    linkStyle 0 stroke:#2196F3,stroke-width:2px;
    linkStyle 1 stroke:#FF9800,stroke-width:2px;
    linkStyle 2 stroke:#4CAF50,stroke-width:2px;
    linkStyle 3 stroke:#f44336,stroke-width:2px;


    ```