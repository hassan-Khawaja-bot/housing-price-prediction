import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/model.pkl")

st.set_page_config(page_title="Housing Price Predictor", layout="centered")

st.title(" California Housing Price Prediction")
st.write("Enter housing details to predict price")

# User inputs
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("House Median Age", value=41)
total_rooms = st.number_input("Total Rooms", value=880)
total_bedrooms = st.number_input("Total Bedrooms", value=129)
population = st.number_input("Population", value=322)
households = st.number_input("Households", value=126)
median_income = st.number_input("Median Income", value=8.3252)

ocean = st.selectbox(
    "Ocean Proximity",
    ["INLAND", "NEAR BAY", "NEAR OCEAN", "ISLAND", "<1H OCEAN"]
)

# Create input dataframe
input_data = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income],
    "ocean_proximity": [ocean]
})

# One-hot encoding
input_data = pd.get_dummies(input_data)

# Align columns
model_features = model.feature_names_in_
input_data = input_data.reindex(columns=model_features, fill_value=0)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f" Predicted House Price: ${prediction:,.2f}")
