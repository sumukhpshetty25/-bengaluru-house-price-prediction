# streamlit_app/app.py

import os
import pandas as pd
import streamlit as st
import pickle
import json
import numpy as np

# Define relative paths to model and columns
model_path = os.path.join('model', 'model.pkl')
columns_path = os.path.join('data', 'columns.json')

# Load the trained model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load columns
with open(columns_path, 'r') as f:
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
