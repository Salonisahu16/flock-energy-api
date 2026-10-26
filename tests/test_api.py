from fastapi.testclient import TestClient

from app.main import app, FlockEnergyClient


client = TestClient(app)


def test_home():
    """Check that the home endpoint works."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Flock Energy API Client is running"
    )


def test_search_meters(monkeypatch):
    """Test meter search without calling the real portal."""

    def mock_search_meters(self, query="", page=1):
        return {
            "data": [
                {
                    "meterId": "J100001",
                    "serialNo": "GE84132",
                    "make": "L&T",
                    "phaseType": "single",
                    "installStatus": "Installed",
                    "dtCode": "DT-002",
                }
            ]
        }

    monkeypatch.setattr(
        FlockEnergyClient,
        "search_meters",
        mock_search_meters,
    )

    response = client.get("/meters")

    assert response.status_code == 200
    assert response.json()["data"][0]["meterId"] == "J100001"


def test_get_meter_energy(monkeypatch):
    """Test energy readings."""

    def mock_get_energy(self, meter_id):
        return {
            "data": [
                {
                    "timestamp": "23/06/2026 23:30",
                    "kwh": "42594.05",
                    "kvah": "46001.58",
                    "voltR": "231",
                }
            ]
        }

    monkeypatch.setattr(
        FlockEnergyClient,
        "get_energy",
        mock_get_energy,
    )

    response = client.get("/meters/J100001/energy")

    assert response.status_code == 200
    assert response.json()["data"][0]["kwh"] == 42594.05


def test_get_meter_geo(monkeypatch):
    """Test geographic coordinates."""

    def mock_get_geo(self, meter_id):
        return {
            "data": {
                "latitude": "26.822136543835608",
                "longitude": "75.90718190602279",
            }
        }

    monkeypatch.setattr(
        FlockEnergyClient,
        "get_geo",
        mock_get_geo,
    )

    response = client.get("/meters/J100001/geo")

    assert response.status_code == 200
    assert response.json()["data"]["latitude"] == 26.822136543835608

