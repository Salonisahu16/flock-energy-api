# Flock Energy API Client

A Python-based API client and FastAPI wrapper for retrieving electricity meter information, energy readings, and geographic coordinates from the Flock Energy portal.

## Features

* Search meters using a query and page number.
* Retrieve energy readings for a specific meter.
* Retrieve geographic coordinates for a meter.
* Validate API responses using Pydantic models.
* Expose endpoints through FastAPI.
* Run automated tests using pytest.

## Tech Stack

* Python
* FastAPI
* HTTPX
* Pydantic
* python-dotenv
* pytest

## Project Structure

```text
flock-energy-api/
├── app/
│   ├── __init__.py
│   ├── client.py
│   ├── main.py
│   └── models.py
├── tests/
│   └── test_api.py
├── .env.example
├── .gitignore
├── openapi.json
├── PROTOCOL.md
├── README.md
├── REFLECTION.md
└── requirements.txt
```

## Setup Instructions

### 1. Clone the Repository

Replace the placeholder with your GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd flock-energy-api
```

### 2. Create a Virtual Environment

For Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a template.

If an authorized session token is required, configure it in `.env`:

```env
FLOCK_SESSION_TOKEN=your_session_token_here
```

Never commit `.env` or real session tokens to GitHub. Independent Python authentication has not yet been verified.

### 5. Start the API Server

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

## Available Endpoints

| Method | Endpoint                    | Description                     |
| ------ | --------------------------- | ------------------------------- |
| GET    | `/`                         | Check API status                |
| GET    | `/meters`                   | Search meters                   |
| GET    | `/meters/{meter_id}/energy` | Retrieve energy readings        |
| GET    | `/meters/{meter_id}/geo`    | Retrieve geographic coordinates |

## Sample Requests

Start the local service:

```bash
uvicorn app.main:app --reload
```

The examples below assume the service is running at `http://127.0.0.1:8000`.

### Check service health

```bash
curl http://127.0.0.1:8000/
```

### Search meters

```bash
curl "http://127.0.0.1:8000/meters?q=&page=1"
```

### Retrieve energy readings

```bash
curl http://127.0.0.1:8000/meters/J100001/energy
```

### Retrieve geographic coordinates

```bash
curl http://127.0.0.1:8000/meters/J100001/geo
```

These endpoints call the upstream portal. Successful live requests depend on valid authentication and upstream availability. The automated tests use mocked client methods and do not require live portal access.

## Design Decisions and Trade-offs

* **FastAPI:** Provides a small REST API and generates an OpenAPI specification automatically.
* **HTTPX:** Provides an HTTP client for communicating with the upstream portal.
* **Pydantic:** Validates response structures and converts numeric strings to numeric values.
* **Environment-based credentials:** Keeps the session token out of source code and version control.
* **Limited scope:** Three observed read-only operations were prioritised over attempting to reconstruct the entire portal within the time budget.
* **No cache or local index:** These were left out because data freshness requirements, dataset size, and bulk access behavior have not yet been established.

## Intentionally Skipped

The network hierarchy, additional portal sections, bulk-data access, caching, and a separate frontend were not implemented. The available time was used to build and test the API wrapper for the three observed operations.

## Documentation

* [Portal protocol and observations](PROTOCOL.md)
* [API specification](openapi.json)
* [Engineering reflection](REFLECTION.md)


### Search Meters

`GET /meters?q=&page=1`

* `q`: Optional search query.
* `page`: Page number; defaults to `1`.

### Retrieve Energy Readings

`GET /meters/J100001/energy`

Returns energy readings containing fields such as timestamp, kWh, kVAh, and voltage.

### Retrieve Geographic Coordinates

`GET /meters/J100001/geo`

Returns the observed latitude and longitude for the specified meter.

## Run Tests

```bash
python -m pytest -v
```

The current tests mock upstream client methods, so they can run without depending on live portal availability.

## Protocol Documentation

See [PROTOCOL.md](PROTOCOL.md) for the observed upstream endpoints, response fields, authentication observations, and known limitations.

## OpenAPI Specification

The `openapi.json` file describes this project's FastAPI wrapper. It is not a complete specification of the original portal API.

## Assumptions and Limitations

* The upstream endpoints were observed through an authenticated browser session.
* Independent Python authentication has not been verified.
* Pagination metadata, rate limits, retry behavior, and complete error schemas are not yet established.
* The complete API surface of Ops Desk, Transformer, and Ultra Major Ops has not been investigated.
* This implementation focuses on three read-only meter operations.

## Future Improvements

* Improve upstream error handling.
* Add tests for invalid inputs and upstream failures.
* Verify authentication and unauthorized-response behavior.
* Investigate pagination and rate limits.
* Document additional endpoints if they are required and can be verified.

## Disclaimer

This project is an independent engineering exercise based on observed portal behavior. It does not claim to document every endpoint or behavior of the original portal.
