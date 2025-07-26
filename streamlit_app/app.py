# streamlit_app/app.py

import streamlit as st
import pickle
import json
import numpy as np

# Load model and columns
with open('C:/Users/Sumukh P Shetty/Desktop/House_Price_Predict/model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('C:/Users/Sumukh P Shetty/Desktop/House_Price_Predict/data/datacolumns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']
    locations = [col for col in data_columns if col not in ['total_sqft', 'bath', 'bhk']]

# Streamlit UI
st.title("🏠 Bengaluru House Price Predictor")

# Input fields
sqft = st.number_input("Total Square Feet", value=1000)
bhk = st.selectbox("Number of Bedrooms (BHK)", [1, 2, 3, 4, 5])
bath = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
location = st.selectbox("Location", sorted(locations))

if st.button("Predict Price"):
    # Create input vector
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    predicted_price = model.predict([x])[0]
    st.success(f"Estimated Price: ₹ {predicted_price:.2f} Lakhs")
