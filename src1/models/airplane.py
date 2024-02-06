from datetime import datetime
from pydantic import BaseModel

class Airplane(BaseModel):
    registration_number: str
    model: str
    flight_type: str  # 'DOM' for domestic, 'INT' for international
    source: str
    destination: str = "Springvale"

class Landing(BaseModel):
    airplane: Airplane
    reason: str
    landing_time: datetime
    runway_used: int

class Departure(BaseModel):
    airplane: Airplane
    gate: int
    departure_time: datetime
    runway_used: int
