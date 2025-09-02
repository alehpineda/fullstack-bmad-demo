## 5. CI/CD Pipeline

Two separate CI/CD pipelines will be established using GitHub Actions to ensure the quality of the backend and frontend codebases independently.

#### 5.1. Backend CI Pipeline (`.github/workflows/ci.yaml`)

This workflow runs on every pull request targeting the `master` branch.

*   **Trigger:** `on: [pull_request]`
*   **Jobs:**
    1.  **`lint-and-test`**:
        *   **Setup:** Checks out the code and sets up Python 3.13.
        *   **`uv` Installation:** Uses the official `astral-sh/setup-uv@v1` action for fast and reliable setup. Caching is enabled.
        *   **Linting:** Runs `ruff format --check .` and `ruff check .` to enforce code style and quality.
        *   **Type Checking:** Runs `mypy .` to validate type hints.
        *   **Testing:** Runs `pytest` to execute all unit and integration tests.
    2.  **`smoke-test`**:
        *   **Needs:** `lint-and-test`
        *   **Description:** Runs after tests pass to ensure the containerized application starts and responds correctly.
        *   **Steps:**
            *   Builds and starts the services using `docker compose up -d`.
            *   Waits for the backend health check to pass.
            *   Executes `curl http://localhost:8080/api/pokemon/25` and asserts a `200 OK` response, validating the full stack.

#### 5.2. Frontend CI Pipeline (`.github/workflows/frontend-ci.yaml`)

This workflow validates the static frontend assets.

*   **Trigger:** `on: [pull_request]`
*   **Jobs:**
    1.  **`build-and-lint`**:
        *   **Setup:** Checks out the code and sets up Node.js.
        *   **Dependencies:** Installs `tailwindcss` and `htmlhint`.
        *   **Build:** Runs the Tailwind CSS build process to generate the final stylesheet.
        *   **Linting:** Runs `htmlhint` on all `.html` files to check for basic syntax and best practice violations.
