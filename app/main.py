from fastapi import FastAPI, HTTPException, Query

from app.client import FlockEnergyClient
from app.models import (
    MeterSearchResponse,
    EnergyResponse,
    GeoResponse,
)

app = FastAPI(
    title="Flock Energy API Client",
    description="API for retrieving meter information, energy readings, and geographic data.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Flock Energy API Client is running",
        "docs": "/docs",
    }


@app.get("/meters", response_model=MeterSearchResponse)
def search_meters(
    q: str = Query(default="", description="Meter search query"),
    page: int = Query(default=1, ge=1),
):
    try:
        with FlockEnergyClient() as client:
            return client.search_meters(query=q, page=page)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Failed to fetch meter search results: {exc}",
        )


@app.get("/meters/{meter_id}/energy", response_model=EnergyResponse)
def get_meter_energy(meter_id: str):
    try:
        with FlockEnergyClient() as client:
            return client.get_energy(meter_id)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Failed to fetch energy readings: {exc}",
        )


@app.get("/meters/{meter_id}/geo", response_model=GeoResponse)
def get_meter_geo(meter_id: str):
    try:
        with FlockEnergyClient() as client:
            return client.get_geo(meter_id)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Failed to fetch geographic data: {exc}",
        )

