from fastapi import FastAPI
import pandas as pd

from .model_loader import eta_model, crowding_model, crowding_encoder
from .schemas import PredictionInput

app = FastAPI(title="Public Transport Optimization API")

@app.post("/predict")
def predict(data: PredictionInput):
    input_dict = data.dict()
    df = pd.DataFrame([input_dict])

    eta = eta_model.predict(
        df[[
            "hour",
            "day_of_week",
            "is_weekend",
            "route_id",
            "stop_sequence",
            "distance_to_next_stop_km",
            "traffic_level",
            "rain_flag"
        ]]
    )[0]

    crowd_pred = crowding_model.predict(
        df[[
            "hour",
            "day_of_week",
            "is_weekend",
            "route_id",
            "stop_sequence",
            "distance_to_next_stop_km",
            "traffic_level",
            "rain_flag",
            "passenger_count",
            "bus_capacity"
        ]]
    )[0]

    crowd_label = crowding_encoder.inverse_transform([crowd_pred])[0]

    return {
        "predicted_eta_minutes": round(float(eta), 2),
        "crowding_level": crowd_label
    }
