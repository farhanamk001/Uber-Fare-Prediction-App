import streamlit as st
import numpy as np
import joblib
from haversine import haversine
from datetime import datetime

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Uber Fare Prediction",
    page_icon="🚕",
    layout="centered"
)

st.title("🚕 Uber Fare Prediction App")
st.write("Predict Uber fare using pickup & dropoff details ")

# -----------------------------
# Load trained model (joblib)
# -----------------------------
model = joblib.load("uber_fare_model.pkl")

# -----------------------------
# Input Form
# -----------------------------
with st.form("fare_form", clear_on_submit=True):

    pickup_longitude = st.number_input(
        "Pickup Longitude", format="%.6f"
    )
    pickup_latitude = st.number_input(
        "Pickup Latitude", format="%.6f"
    )
    dropoff_longitude = st.number_input(
        "Dropoff Longitude", format="%.6f"
    )
    dropoff_latitude = st.number_input(
        "Dropoff Latitude", format="%.6f"
    )

    passenger_count = st.slider(
        "Passenger Count", min_value=1, max_value=6, value=1
    )

    pickup_date = st.date_input("Pickup Date")
    pickup_time = st.time_input("Pickup Time")

    col1, col2 = st.columns(2)
    with col1:
        predict_btn = st.form_submit_button("💰 Predict Fare")
    with col2:
        clear_btn = st.form_submit_button("🧹 Clear")

# -----------------------------
# Clear button logic
# -----------------------------
# if clear_btn:
#     st.rerun()

# -----------------------------
# Prediction logic
# -----------------------------
if predict_btn:

    # Combine date & time safely
    pickup_datetime = datetime.combine(pickup_date, pickup_time)

    day = pickup_datetime.day
    month = pickup_datetime.month
    year = pickup_datetime.year
    dayofweek = pickup_datetime.weekday()
    hour = pickup_datetime.hour

    # Distance calculation (Haversine)
    loc1 = (pickup_latitude, pickup_longitude)
    loc2 = (dropoff_latitude, dropoff_longitude)
    distance_km = haversine(loc1, loc2)

    # Basic validation
    if distance_km <= 0:
        st.error("❌ Invalid distance. Please check coordinates.")
    else:
        input_data = np.array([[
            passenger_count,
            pickup_longitude,
            pickup_latitude,
            dropoff_longitude,
            dropoff_latitude,
            day,
            month,
            year,
            dayofweek,
            hour,
            distance_km
        ]])

        prediction = model.predict(input_data)

        st.success(
            f"✅ Estimated Uber Fare: **${prediction[0]:.2f} USD**"
        )
