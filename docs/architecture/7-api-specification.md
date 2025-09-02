## 7. API Specification

This section outlines the API endpoints the backend will expose.

#### 7.1. Core JSON API

**Endpoint:** `GET /api/pokemon/{pokemon_id}`
**Description:** Fetches data for a single Pokémon by its ID.

*   **`200 OK`**: Returns a JSON object of the `Pokemon` model.
*   **`404 Not Found`**: Returns a JSON error detail.

#### 7.2. HTMX Web Endpoints

**Endpoint:** `POST /web/pokemon/search`
**Description:** Searches for a Pokémon and returns an HTML partial.

*   **`200 OK` (Success)**: Returns a `text/html` partial displaying the Pokémon card.
*   **`200 OK` (Not Found)**: Returns a `text/html` partial displaying a "not found" message.

#### 7.3. Health Check Endpoint

**Endpoint:** `GET /health`
**Description:** A simple endpoint to verify that the API service is running and available.
*   **`200 OK`**: Returns `{"status": "ok"}`. This is used for container health checks.

#### 7.4. API Rate Limiting

A global, IP-based rate limit of **20 requests per minute** will be implemented using the `slowapi` library to prevent abuse. Exceeding the limit will result in a `429 Too Many Requests` response.
