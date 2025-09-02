"""Simple test to validate the project setup."""


def test_hello_world():
    """A simple 'hello world' test to validate pytest setup."""
    assert True


def test_python_version():
    """Test that we're using Python 3.13+."""
    import sys
    
    assert sys.version_info >= (3, 13)


def test_fastapi_import():
    """Test that FastAPI can be imported."""
    try:
        import fastapi  # noqa: F401
        assert True
    except ImportError:
        assert False, "FastAPI not available"


def test_uvicorn_import():
    """Test that uvicorn can be imported."""
    try:
        import uvicorn  # noqa: F401
        assert True
    except ImportError:
        assert False, "uvicorn not available"


def test_fastapi_app():
    """Test that the FastAPI app can be created."""
    import sys
    import os
    
    # Add the parent directory to the path so we can import main
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, backend_dir)
    
    from main import app
    assert app.title == "Pokémon Search API"
    assert app.version == "0.1.0"