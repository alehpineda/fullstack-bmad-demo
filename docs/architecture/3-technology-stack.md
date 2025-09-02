## 3. Technology Stack

The technology stack is chosen to align with the PRD's constraints (**NFR5**, **NFR6**), emphasizing modern, high-performance, open-source tools.

| Category      | Technology / Tool | Version | Rationale                                                              |
| :------------ | :---------------- | :------ | :--------------------------------------------------------------------- |
| **Backend**   | Python            | 3.13    | Modern, widely-supported language.                                     |
|               | FastAPI           | Latest  | High-performance async web framework with excellent developer tooling. |
|               | Pydantic          | Latest  | Core to FastAPI for robust data validation and serialization.          |
|               | SQLAlchemy        | Latest  | Used in the ingestion script for reliable database interaction.        |
| **Frontend**  | HTML5             | -       | Standard for web content.                                              |
|               | HTMX              | Latest  | Enables modern, dynamic UIs directly from the backend without heavy JS. |
|               | Tailwind CSS      | Latest  | Utility-first CSS framework for rapid, responsive UI development.      |
| **Database**  | SQLite            | 3.x     | Zero-configuration, file-based database ideal for a self-contained app. |
| **DevOps**    | Docker            | Latest  | Containerization for consistent development and deployment.            |
|               | Docker Compose    | Latest  | Orchestrates multi-container application startup.                      |
|               | GitHub Actions    | -       | CI/CD automation for quality assurance.                                |
| **Tooling**   | `uv`              | Latest  | High-performance Python package and environment manager.               |
|               | `ruff`            | Latest  | All-in-one linter and formatter for clean, consistent Python code.     |
|               | `pytest`          | Latest  | Standard framework for testing Python code.                            |
|               | `mypy`            | Latest  | Static type checker to enforce type hints and prevent bugs.            |
