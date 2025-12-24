from pydantic import BaseModel

class PredictionInput(BaseModel):
    hour: int
    day_of_week: int
    is_weekend: int
    route_id: int
    stop_sequence: int
    distance_to_next_stop_km: float
    traffic_level: int
    rain_flag: int
    passenger_count: int
    bus_capacity: int
