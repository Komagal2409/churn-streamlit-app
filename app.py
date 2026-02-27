import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model (1).pkl")
cols = joblib.load("model_columns (1).pkl")

st.title("Churn Prediction")

CreditScore = st.number_input("CreditScore")
Age = st.number_input("Age")
Balance = st.number_input("Balance")
IsActiveMember = st.selectbox("IsActiveMember",[0,1])
EstimatedSalary = st.number_input("EstimatedSalary")

Gender = st.selectbox("Gender",["Male","Female"])
Geography = st.selectbox("Geography",["France","Germany","Spain"])

input_dict = {
    "CreditScore":CreditScore,
    "Age":Age,
    "Balance":Balance,
    "IsActiveMember":IsActiveMember,
    "EstimatedSalary":EstimatedSalary,
    "Gender_Female":1 if Gender=="Female" else 0,
    "Gender_Male":1 if Gender=="Male" else 0,
    "Geography_France":1 if Geography=="France" else 0,
    "Geography_Germany":1 if Geography=="Germany" else 0,
    "Geography_Spain":1 if Geography=="Spain" else 0
}

input_df = pd.DataFrame([input_dict])
input_df = input_df[cols]

if st.button("Predict"):
    pred = model.predict(input_df)
    st.write("Churn" if pred[0]==1 else "No Churn")
