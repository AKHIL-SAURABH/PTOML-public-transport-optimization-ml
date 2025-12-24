import streamlit as st
import requests


st.set_page_config(page_title="Public Transport Optimization", layout="centered")

st.title("🚍 Public Transport Optimization using ML")
st.markdown(
    """
    This dashboard predicts:
    - ⏱️ **Bus Arrival Time (ETA)**
    - 👥 **Crowding Level**
    
    using machine learning models trained on transport patterns.
    """
)


st.header("Enter Trip Details")

with st.form("prediction_form"):
    hour = st.slider("Hour of Day", 0, 23, 9)
    day_of_week = st.selectbox("Day of Week", list(range(7)))
    is_weekend = st.selectbox("Is Weekend?", [0, 1])

    route_id = st.number_input("Route ID", min_value=1, max_value=20, value=5)
    stop_sequence = st.number_input("Stop Sequence", min_value=1, max_value=15, value=7)

    distance = st.slider("Distance to Next Stop (km)", 0.5, 3.0, 1.8)
    traffic_level = st.selectbox("Traffic Level (1=Low, 3=High)", [1, 2, 3])
    rain_flag = st.selectbox("Is it Raining?", [0, 1])

    passenger_count = st.slider("Passenger Count", 0, 50, 40)
    bus_capacity = st.number_input("Bus Capacity", value=50)

    submit = st.form_submit_button("Predict")


if submit:
    payload = {
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend,
        "route_id": route_id,
        "stop_sequence": stop_sequence,
        "distance_to_next_stop_km": distance,
        "traffic_level": traffic_level,
        "rain_flag": rain_flag,
        "passenger_count": passenger_count,
        "bus_capacity": bus_capacity
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success("Prediction Successful!")

            st.metric(
                label="⏱️ Predicted ETA (minutes)",
                value=result["predicted_eta_minutes"]
            )

            st.metric(
                label="👥 Crowding Level",
                value=result["crowding_level"]
            )

        else:
            st.error("API Error. Please check the backend.")

    except Exception as e:
        st.error(f"Connection Error: {e}")


