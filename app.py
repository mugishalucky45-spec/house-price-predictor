import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Rwanda House Price Predictor", page_icon="🏠")

st.title("Rwanda House Price Predictor")
st.write("Estimate the market price of a house in million RWF using a trained multiple linear regression model.")

@st.cache_resource
def load_model():
    return joblib.load("house_price_model.sav")

model = load_model()

# Ranges and defaults are based on the cleaned training dataset.
area = st.number_input("Area (m²)", min_value=26.0, max_value=1200.0, value=120.0)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=6, value=3, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=2, step=1)
age = st.number_input("House Age (years)", min_value=0.4, max_value=75.0, value=5.0)
distance = st.number_input("Distance to City (km)", min_value=0.07, max_value=85.0, value=7.0)
parking = st.number_input("Parking Spaces", min_value=0, max_value=3, value=2, step=1)
neighborhood = st.selectbox("Neighborhood", ['Gasabo', 'Huye', 'Kicukiro', 'Kigali City', 'Musanze', 'Nyarugenge'])

if st.button("Predict House Price"):
    x = pd.DataFrame([{"Area_m2": area,
                        "Bedrooms": bedrooms,
                        "Bathrooms": bathrooms,
                        "House_Age_Years": age,
                        "Distance_to_City_km": distance,
                        "Parking_Spaces": parking,
                        "Neighborhood": neighborhood}])
    pred = model.predict(x)[0]
    st.success(f"Estimated house price: {pred:.2f} million RWF")
