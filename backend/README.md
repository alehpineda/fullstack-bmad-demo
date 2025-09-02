# Backend

FastAPI backend for the Pokémon search application.

## Prerequisites

- Python 3.13+
- `uv` package manager (see [installation instructions](https://docs.astral.sh/uv/getting-started/installation/))

## Environment Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate the virtual environment with dependencies:
   ```bash
   uv sync --dev
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

## Development Commands

All commands should be run from the `backend` directory.

### Running with uv

You can run commands directly with `uv run` without manually activating the virtual environment:

```bash
# Run the application
uv run uvicorn main:app --reload

# Run tests
uv run pytest

# Run linting
uv run ruff check .

# Format code
uv run ruff format .
```

### Running with activated environment

If you prefer to activate the virtual environment first:

```bash
# Activate environment
source .venv/bin/activate

# Run the application
uvicorn main:app --reload

# Run tests
pytest

# Run linting
ruff check .

# Format code
ruff format .
```

## Dependencies

### Core Dependencies
- **FastAPI**: High-performance async web framework
- **uvicorn**: ASGI server for FastAPI

### Development Dependencies
- **pytest**: Testing framework
- **ruff**: Linting and formatting tool

## Project Structure

```
backend/
├── .venv/              # Virtual environment (created by uv)
├── tests/              # Test files
│   └── test_setup.py   # Setup validation tests
├── main.py             # Main application entry point
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Dependency lock file
└── README.md           # This file
```
