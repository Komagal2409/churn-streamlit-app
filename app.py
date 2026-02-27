import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction 🚀")

credit_score = st.number_input("Credit Score")
age = st.number_input("Age")
balance = st.number_input("Balance")
salary = st.number_input("Estimated Salary")

if st.button("Predict"):
    features = np.array([[credit_score, age, balance, salary]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")