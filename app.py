import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.title("House Price Predictor")

area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(features)
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
