import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
import os

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
geo_encoder = joblib.load(os.path.join(BASE_DIR, "geo_encoder.pkl"))
gender_encoder = joblib.load(os.path.join(BASE_DIR, "gender_encoder.pkl"))
geo_encoder = joblib.load("geo_encoder.pkl")
gender_encoder = joblib.load("gender_encoder.pkl")

st.title("🏦 Bank Customer Churn Predictor")

st.write("Enter customer details below to predict churn")

# Inputs
credit_score = st.slider("Credit Score", 300, 900, 600)
age = st.slider("Age", 18, 92, 30)
tenure = st.slider("Tenure (Years with Bank)", 0, 10, 3)
balance = st.number_input("Account Balance", 0.0, 250000.0, 50000.0)
num_products = st.slider("Number of Products", 1, 4, 1)

geography = st.selectbox("Geography", geo_encoder.classes_)
gender = st.selectbox("Gender", gender_encoder.classes_)

has_card = st.selectbox("Has Credit Card", [0, 1])
active_member = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

# Predict button
if st.button("Predict Churn"):

    # Encode inputs
    geo_encoded = geo_encoder.transform([geography])[0]
    gender_encoded = gender_encoder.transform([gender])[0]

    # Create input dataframe
    input_data = pd.DataFrame([[
        credit_score, geo_encoded, gender_encoded, age, tenure,
        balance, num_products, has_card, active_member, salary
    ]], columns=[
        "CreditScore", "Geography", "Gender", "Age", "Tenure",
        "Balance", "NumOfProducts", "HasCrCard", "IsActiveMember", "EstimatedSalary"
    ])

    # Predict
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Show result
    if prediction == 1:
        st.error(f"⚠️ Customer likely to churn (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer likely to stay (Probability: {1-probability:.2f})")
