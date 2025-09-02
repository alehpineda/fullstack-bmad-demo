# 4. Technical Assumptions

## 4.1. Repository Structure: Monorepo
The project will be developed within a single monorepo. This structure is mandated to simplify project setup, dependency management, and the overall development workflow for this self-contained showcase.

## 4.2. Service Architecture
The application will be built as a simple, self-contained monolith. It will follow a classic 3-tier architecture (Frontend -> Backend API -> Database) to ensure the design is easy to understand, fast to develop, and straightforward to demonstrate.

## 4.3. Testing Requirements
A baseline of automated testing is required to validate the quality and correctness of the AI-generated code.
*   **Scope:** The testing suite must include **Unit Tests** for key logic and **Integration Tests** for the API endpoint.
*   **Enforcement:** These automated tests **must be integrated into the GitHub Actions CI/CD pipeline** and configured to run automatically on every pull request as a mandatory status check before merging.

## 4.4. Additional Technical Assumptions and Requests
The following technology stack is mandated by the Project Brief to meet the specific goals of the showcase:
*   **Backend (Python & FastAPI):** Chosen for its development speed, modern features, and automatic documentation generation, which aligns with the goal of showcasing a rapid, well-documented process.
*   **Frontend (HTMX & Tailwind CSS):** Chosen to demonstrate a modern, lightweight approach to frontend development that avoids heavy JavaScript frameworks, reinforcing the theme of speed and simplicity.
*   **Database (SQLite):** Chosen for its zero-configuration, file-based nature, making the project entirely self-contained and easy to run for demonstration purposes.
*   **Infrastructure (Docker):** The entire application must be containerized to ensure a consistent, one-command startup experience for the showcase.
*   **Development Workflow (GitHub Issues & Copilot Agent):** This is a core, non-negotiable component. The process of converting stories to issues that are then implemented by the Copilot agent is a primary element to be demonstrated.

---