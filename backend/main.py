"""FastAPI backend for Pokémon search application."""

from fastapi import FastAPI

app = FastAPI(
    title="Pokémon Search API",
    description="FastAPI backend for searching Pokémon information",
    version="0.1.0",
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Pokémon Search API"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


def main():
    """Main function for development server."""
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
