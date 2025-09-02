# 6. Epic 1 Details: Core MVP - Search by ID

### Story 1.1: Python Project Scaffolding
*   **As a developer,** I want the Python backend project to be scaffolded with `uv` for environment management and `ruff` and `pytest` for quality tooling, **so that** I have a modern, standardized foundation for development.
*   **Acceptance Criteria:**
    1.  The `backend` directory is configured as a `uv` project.
    2.  A `pyproject.toml` file in the `backend` directory is configured with the initial project dependencies: `fastapi` and `uvicorn`.
    3.  The `pyproject.toml` also includes development dependencies: `pytest` for testing and `ruff` for linting.
    4.  A `uv` virtual environment can be successfully created and activated from within the `backend` directory.
    5.  The existing `.gitignore` file is updated to exclude the `.venv` directory.

### Story 1.2: Async Pokémon Data Ingestion
*   **As a developer,** I want an efficient, asynchronous script that uses `httpx` to fetch detailed data for the first 151 Pokémon and batch-inserts it into the database, **so that** the data ingestion process is fast and robust.
*   **Acceptance Criteria:**
    1.  The data population script uses the `httpx` library to make asynchronous HTTP requests to the PokeAPI.
    2.  The script leverages `asyncio` to run the API calls for all 151 Pokémon concurrently.
    3.  The script uses the defined SQLAlchemy models to prepare the data for the database.
    4.  After processing the API responses, the script inserts the new records into the database in batches to ensure efficient writes.
    5.  The script is idempotent: if run again, it will not create duplicate Pokémon entries or raise an error.
    6.  The final `pokedex.db` file is correctly created and populated with the data for the first 151 Pokémon.

### Story 1.3: Backend API Endpoint
*   **As a frontend developer,** I want a backend API endpoint that returns a single Pokémon's data in JSON format when I provide its ID, **so that** I can display that data in the user interface.
*   **Acceptance Criteria:**
    1.  A FastAPI application provides a GET endpoint at `/api/pokemon/{pokemon_id}`.
    2.  When a valid ID is provided (e.g., `/api/pokemon/25`), the endpoint returns a `200 OK` status with a JSON body containing the `id`, `name`, and `sprite_url`.
    3.  When an invalid or non-existent ID is provided (e.g., `/api/pokemon/999`), the endpoint returns a `404 Not Found` status.
    4.  The endpoint is covered by automated unit and integration tests using `pytest`.

### Story 1.4: Search UI and Result Display
*   **As a user,** I want a simple web page where I can enter a Pokémon's ID and see its name and image, **so that** I can find information about a specific Pokémon.
*   **Acceptance Criteria:**
    1.  The page displays a text input for the Pokémon ID and a "Search" button.
    2.  Initiating a search triggers a call to the `/api/pokemon/{pokemon_id}` backend endpoint.
    3.  While the data is being fetched, a loading indicator is displayed for a minimum of 300ms.
    4.  If the API returns a Pokémon, its ID, name, and sprite image are displayed.
    5.  If the API returns a 404 error, a "Pokémon not found" message is displayed.
    6.  The UI is responsive and usable on both desktop and mobile viewports.

### Story 1.5: Production-Ready Containerization and CI
*   **As a developer,** I want the application containerized using optimized, production-ready images and have a CI pipeline, **so that** I can ensure a consistent, reliable, and efficient build and test process.
*   **Acceptance Criteria:**
    1.  A `docker-compose.yml` file orchestrates the application services.
    2.  The backend service is built using a `python-slim` base image.
    3.  The frontend service uses a standard `nginx` base image to serve the static HTML content.
    4.  Running `docker compose up` successfully builds and starts the `nginx` and `python-slim` services.
    5.  The application is fully functional, with the Nginx container correctly proxying requests to the Python backend service.
    6.  A GitHub Actions workflow is configured to run `ruff` for linting and `pytest` for tests on every pull request.
    7.  The pull request in GitHub shows a "pass" or "fail" status from the CI check.

---