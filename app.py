import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model (1).pkl")
cols = joblib.load("model_columns (1).pkl")

def bg_color():
    st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #ffdde1, #ee9ca7);
    }

    section[data-testid="stSidebar"] {
        background-color: #ff69b4;
    }

    .stButton>button {
        background-color: #ff1493;
        color: white;
        border-radius: 12px;
        font-weight: bold;
    }
        .quote {
        font-size:20px;
        font-style: italic;
        text-align:center;
        color:#4a044e;
        padding:10px;
    }
     .feature-box {
        background-color:white;
        padding:20px;
        border-radius:15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        text-align:center;
    }
        </style>
        """,
        unsafe_allow_html=True
    )

bg_color()

st.title("Churn Prediction")

menu = st.sidebar.selectbox("Menu", ["Home", "Dashboard", "Predict"])
st.markdown('<p class="quote">"Understanding  Customer behaviour is the key to the Organization Success."</p>', unsafe_allow_html=True)
st.header("""
This AI-powered application predicts whether a customer is likely to leave a bank.
Using Machine Learning, businesses can take proactive steps to retain customers.
""")


if menu == "Home":
    st.header("Welcome to Home Page")

Name = st.text_input("Enter Your Name")
Email = st.text_input("Enter your Email")
Date = st.text_input("Enter The Date")

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

    new_data = {
        "Name": name,
        "Email": email,
        "Date": date,
        "Prediction": prediction,
        "Timestamp": datetime.now()
    }

    df = pd.DataFrame([new_data])

    file_path = "employee_predictions.csv"

    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    st.success(" Data Saved Successfully!")
    
    st.header("Dashboard")

if os.path.exists("employee_predictions.csv"):
    data = pd.read_csv("employee_predictions.csv")
    st.dataframe(data)
else:
    st.info("No predictions saved yet.")
    













