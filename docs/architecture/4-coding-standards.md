## 4. Coding Standards

To ensure code quality, maintainability, and consistency, all Python code contributed to the backend must adhere to the following standards:

*   **PEP 8 Compliance:** All code will be formatted according to the PEP 8 style guide. This will be enforced automatically by the `ruff` formatter.
*   **Type Hinting:** All functions and methods must include type hints for arguments and return values. This will be enforced by `mypy`.
*   **Linting:** Code will be checked against a strict set of linting rules defined in `pyproject.toml` and enforced by `ruff`.

These checks will be run automatically as part of the CI/CD pipeline.
