from pydantic import BaseModel, ConfigDict


# Meter ki details ko represent karega
class Meter(BaseModel):
    model_config = ConfigDict(extra="ignore")

    meterId: str
    serialNo: str
    make: str
    phaseType: str
    installStatus: str
    dtCode: str


# Meter search API ka response
class MeterSearchResponse(BaseModel):
    data: list[Meter]


# Ek energy reading ki details
class EnergyReading(BaseModel):
    model_config = ConfigDict(extra="ignore")

    timestamp: str
    kwh: float
    kvah: float
    voltR: float


# Energy API ka response
class EnergyResponse(BaseModel):
    data: list[EnergyReading]


# Meter ki geographical location
class GeoData(BaseModel):
    latitude: float
    longitude: float


# Geo API ka response
class GeoResponse(BaseModel):
    data: GeoData