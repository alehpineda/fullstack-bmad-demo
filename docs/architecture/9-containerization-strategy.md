## 9. Containerization Strategy

The application will be fully containerized using Docker for development and production.

#### 9.1. Backend Service (`Dockerfile.backend`)

```dockerfile
# Dockerfile.backend
FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/
WORKDIR /app
COPY backend/pyproject.toml backend/uv.lock* ./
RUN uv sync --frozen --no-cache
COPY backend/ /app/
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 9.2. Frontend Service (`Dockerfile.frontend`)

```dockerfile
# Dockerfile.frontend
FROM nginx:latest
COPY frontend/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```
*(A corresponding `nginx.conf` file will be created to serve static files and reverse proxy to the backend.)*

#### 9.3. Orchestration (`docker-compose.yml`)

A `docker-compose.yml` file will orchestrate the services, enabling one-command startup (`docker compose up`) with live reloading for development. It will include a health check to ensure the backend is ready before accepting traffic.

```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    volumes:
      - ./backend:/app
      - ./data:/app/data
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    environment:
      - DATABASE_URL=sqlite:///./data/pokedex.db
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      timeout: 5s
      retries: 5

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "8080:80"
    depends_on:
      backend:
        condition: service_healthy

volumes:
  data:
```
