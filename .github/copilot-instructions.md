# Fullstack BMAD Demo - GitHub Copilot Instructions

**ALWAYS reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Project Overview

This is a fullstack Pokémon search application built using the BMAD (Build-Measure-Adapt-Document) development method. The project serves as a demonstration of AI-assisted development workflows and is currently in early development stages with a functional FastAPI backend.

## Working Effectively

### Repository Setup and Dependencies

**CRITICAL FIRST STEP**: Install uv package manager before anything else:
```bash
pip3 install uv --user
export PATH="$HOME/.local/bin:$PATH"
```

Navigate to the backend directory for all backend operations:
```bash
cd backend
```

Bootstrap the backend environment and dependencies:
```bash
uv sync --dev
```
**TIMING**: 
- First time: 3-4 minutes (downloads Python 3.13.7 automatically). NEVER CANCEL.
- Subsequent runs: <1 second

### Development Commands

All backend commands should be run from the `backend/` directory:

**Run tests**:
```bash
uv run pytest -v
```
**TIMING**: <1 second. NEVER CANCEL - tests complete quickly.

**Run linting**:
```bash
uv run ruff check .
```
**TIMING**: <1 second

**Format code**:
```bash
uv run ruff format .
```
**TIMING**: <1 second

**Start development server**:
```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
**TIMING**: Server starts in ~3 seconds. NEVER CANCEL.

**Alternative server startup** (using the main() function):
```bash
uv run python main.py
```

## Validation Scenarios

**ALWAYS test these scenarios after making changes to ensure functionality**:

### Backend API Validation
1. Start the server: `uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000`
2. Test root endpoint: `curl http://localhost:8000/`
   - Expected: `{"message":"Welcome to the Pokémon Search API"}`
3. Test health endpoint: `curl http://localhost:8000/health`
   - Expected: `{"status":"healthy"}`
4. Test API documentation: Open `http://localhost:8000/docs` in browser
   - Expected: Swagger UI interface loads successfully
5. Test OpenAPI spec: `curl http://localhost:8000/openapi.json`
   - Expected: Valid JSON schema returned

### Complete Development Workflow
ALWAYS run this complete sequence when validating changes:
```bash
cd backend
uv sync --dev                    # Setup dependencies
uv run pytest -v                # Run all tests
uv run ruff check .             # Check linting
uv run ruff format .             # Format code
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
SERVER_PID=$!
sleep 5
curl http://localhost:8000/      # Test API
curl http://localhost:8000/health
kill $SERVER_PID                 # Stop server
```

## Technology Stack and Current Status

### Implemented and Working
- **Backend**: Python 3.13.7 with FastAPI framework
- **Package Management**: uv (modern Python package manager)
- **Testing**: pytest with 5 passing setup validation tests
- **Code Quality**: ruff for linting and formatting
- **Server**: uvicorn ASGI server with hot reloading
- **API Documentation**: Automatic OpenAPI/Swagger documentation generation

### Planned but Not Yet Implemented
- **Frontend**: HTMX + Tailwind CSS (architecture documented but not built)
- **Database**: SQLite with Pokémon data ingestion scripts
- **Containerization**: Docker and docker-compose setup
- **CI/CD**: GitHub Actions workflows for testing and deployment
- **Additional API Endpoints**: Pokémon search functionality

## Project Structure

```
fullstack-bmad-demo/
├── .github/
│   ├── chatmodes/           # BMAD method chat modes
│   └── copilot-instructions.md  # This file
├── .bmad-core/              # BMAD method configuration and workflows  
├── backend/                 # FastAPI backend application
│   ├── main.py             # Main application entry point
│   ├── tests/              # Test suite
│   ├── pyproject.toml      # Python project configuration
│   ├── uv.lock            # Dependency lock file
│   └── README.md           # Backend-specific documentation
├── docs/                   # Project documentation
│   ├── prd.md             # Product Requirements Document
│   ├── architecture.md    # System architecture specification
│   └── [other docs]
└── README.md              # Project overview
```

## Key Development Guidelines

### Code Quality Requirements
- **ALWAYS run linting before committing**: `uv run ruff check .`
- **ALWAYS format code**: `uv run ruff format .`  
- **ALWAYS run the full test suite**: `uv run pytest -v`
- **Type hints are required** for all functions (enforced by future mypy integration)

### Testing Strategy
- All code changes MUST include corresponding tests
- Tests MUST pass before committing changes
- Use pytest for all testing
- Integration tests should validate API endpoints end-to-end

### Environment Requirements
- **Python**: 3.13+ (automatically managed by uv)
- **uv**: Latest version for package management
- **OS**: Linux/macOS/Windows (cross-platform)

## Common Development Tasks

### Adding New API Endpoints
1. Add endpoint to `backend/main.py`
2. Add corresponding tests to `backend/tests/`
3. Run validation workflow:
   ```bash
   uv run pytest -v
   uv run ruff check .
   uv run ruff format .
   ```
4. Test manually with server running

### Debugging Issues
1. Check server logs when running `uv run uvicorn main:app --reload`
2. Use FastAPI automatic docs at `http://localhost:8000/docs` for API testing
3. Run tests in verbose mode: `uv run pytest -v -s`

### Performance Expectations
- **Dependency sync**: <1 second (after initial setup)
- **Test execution**: <1 second for current test suite
- **Linting**: <0.1 seconds
- **Server startup**: ~3 seconds
- **API response time**: <200ms for current endpoints

## Future Development Notes

Based on the architecture documentation in `docs/architecture.md`, the next development phases will include:

1. **Database Layer**: SQLite integration with SQLAlchemy models
2. **Data Ingestion**: Asynchronous script to populate Pokémon data from PokeAPI  
3. **Frontend Implementation**: HTMX-based user interface with Tailwind CSS
4. **Containerization**: Docker and docker-compose setup
5. **CI/CD Pipeline**: GitHub Actions for automated testing and deployment

When these components are implemented, update these instructions with:
- New validation scenarios
- Additional timing requirements  
- Extended build and test procedures
- Integration testing workflows

## Troubleshooting

### Common Issues
- **uv not found**: Install with `pip3 install uv --user` and ensure `~/.local/bin` is in PATH
- **Python version mismatch**: uv automatically downloads Python 3.13.7 on first run
- **Port already in use**: Change port in uvicorn command or kill existing processes
- **Import errors**: Ensure you're in the `backend/` directory when running commands

### Emergency Reset
If environment becomes corrupted:
```bash
cd backend
rm -rf .venv
uv sync --dev
```

---

**Remember**: This project is designed to showcase the BMAD method for AI-assisted development. Always follow the complete validation workflow and maintain high code quality standards.