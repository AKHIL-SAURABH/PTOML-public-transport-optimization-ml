import joblib
import os

# Get absolute path to this file (app/model_loader.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths to models/
MODELS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "models"))

eta_model = joblib.load(os.path.join(MODELS_DIR, "eta_model.pkl"))
crowding_model = joblib.load(os.path.join(MODELS_DIR, "crowding_model.pkl"))
crowding_encoder = joblib.load(os.path.join(MODELS_DIR, "crowding_encoder.pkl"))
