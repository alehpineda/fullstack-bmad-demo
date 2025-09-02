## 2. High-Level Architecture

The application will follow a classic **three-tier architecture**, containerized for portability and ease of deployment. This model provides a clear separation of concerns between presentation, application logic, and data storage.

#### 2.1. System Components

1.  **Frontend (Presentation Tier):** A static web interface built with HTML, Tailwind CSS, and HTMX. It will be served by an Nginx web server.
2.  **Backend (Application Tier):** A Python-based API built with FastAPI. This service will handle business logic, data processing, and communication with the database.
3.  **Database (Data Tier):** A simple SQLite database to store Pokémon data.

#### 2.2. Architecture Diagram

```mermaid
graph TD
    subgraph "User's Browser"
        A[User]
    end

    subgraph "Docker Environment"
        B[Nginx Frontend]
        C[FastAPI Backend]
        D[SQLite Database]
    end

    A -- HTTPS Request --> B
    B -- Serves index.html & CSS --> A
    A -- HTMX Search Request --> B
    B -- Reverse Proxy to /api --> C
    C -- Queries for Pokémon --> D
    D -- Returns Pokémon Data --> C
    C -- Returns HTML Partial --> B
    B -- Delivers HTML Partial --> A

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#cfc,stroke:#333,stroke-width:2px
```

#### 2.3. Data Ingestion Flow

A one-time data ingestion script will populate the SQLite database from the public PokeAPI. This script is run manually once during setup or can be integrated into the container build process if needed.

```mermaid
sequenceDiagram
    participant Developer
    participant Ingestion Script
    participant PokeAPI
    participant SQLite DB

    Developer->>Ingestion Script: Run script (e.g., `uv run python scripts/populate_db.py`)
    activate Ingestion Script
    Ingestion Script->>PokeAPI: Asynchronously fetch data for 151 Pokémon
    activate PokeAPI
    PokeAPI-->>Ingestion Script: Return Pokémon data
    deactivate PokeAPI
    Ingestion Script->>SQLite DB: Batch insert Pokémon records
    activate SQLite DB
    SQLite DB-->>Ingestion Script: Confirm writes
    deactivate SQLite DB
    Ingestion Script-->>Developer: Log completion
    deactivate Ingestion Script
```
