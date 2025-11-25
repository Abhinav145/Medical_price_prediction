import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.set_page_config(
    page_title="Medical Cost Prediction",
    page_icon="💊",
    layout="centered",
)

st.markdown("""
    <h1 style='text-align:center; color:#4CAF50;'>💊 Medical Cost Prediction App</h1>
    <p style='text-align:center;'>Enter patient details below to estimate medical insurance charges.</p>
""", unsafe_allow_html=True)

st.write("")

st.sidebar.header("About")
st.sidebar.info("""
This app predicts medical insurance cost using a trained Machine Learning model.
""")

age = st.number_input("Age", min_value=1, max_value=100, step=1)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)

sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker?", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Correct input format
input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "sex": [sex],
    "smoker": [smoker],
    "region": [region]
})

if st.button("Predict Medical Cost 💵"):
    pred = pipe.predict(input_data)[0]
    st.success(f"Predicted Medical Cost: **₹{pred:,.2f}**")
