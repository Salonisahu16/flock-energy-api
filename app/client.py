import os

import httpx
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

BASE_URL = "https://urja-ops.flockenergy.tech"

# Cookie name discovered from the portal.
COOKIE_NAME = "__Secure-better-auth.session_token"


class FlockEnergyClient:
    """Client for accessing the Flock Energy portal APIs."""

    def __init__(self, session_token=None):
        # Read the session token from the environment if not provided.
        token = session_token or os.getenv("FLOCK_SESSION_TOKEN")

        # Create an HTTP client with a base URL and timeout.
        self.client = httpx.Client(
            base_url=BASE_URL,
            timeout=20.0,
            follow_redirects=True,
        )

        # Attach the session cookie only when a token is configured.
        if token:
            self.client.cookies.set(COOKIE_NAME, token)

    def search_meters(self, query="", page=1):
        """Search meters and return the API response."""
        response = self.client.get(
            "/portal/meters/search",
            params={"q": query, "page": page},
        )
        response.raise_for_status()
        return response.json()

    def get_energy(self, meter_id):
        """Fetch energy readings for a meter."""
        response = self.client.get(
            f"/portal/meters/{meter_id}/energy"
        )
        response.raise_for_status()
        return response.json()

    def get_geo(self, meter_id):
        """Fetch geographic coordinates for a meter."""
        response = self.client.get(
            f"/portal/meters/{meter_id}/geo"
        )
        response.raise_for_status()
        return response.json()

    def close(self):
        """Close the HTTP client and release its resources."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

