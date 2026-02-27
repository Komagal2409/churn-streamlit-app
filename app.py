import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score")
age = st.number_input("Age")
balance = st.number_input("Balance")
isactive = st.number_input("IsActiveMember")
salary = st.number_input("Estimated Salary")
Female = st.number_input("Gender_Female")
Male = st.number_input("Gender_Male")
France = st.number_input("Geography_France")
Germany = st.number_input("Geography_Germany")
Spain = st.number_input("Geography_Spain")

if st.button("Predict"):
    features = np.array([[credit_score, age, balance, salary, isactive, Female, Male, France, Spain, Germany]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")

