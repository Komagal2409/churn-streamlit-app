import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model (1).pkl")
cols = joblib.load("model_columns (1).pkl")

def bg_color():
    st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
        background-color: #ff69b4;
    }

    .stApp {
        background-color: #fff0f5;
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
st.image("https://media.licdn.com/dms/image/v2/C5612AQF7E7hVZoiX5w/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1594306960827?e=2147483647&v=beta&t=GY2dIrJr3ig7XaieFsaTB_9kdBPP4oAelgt2Y_ezpMU", use_container_width=True)
st.header("""
This AI-powered application predicts whether a customer is likely to leave a bank.
Using Machine Learning, businesses can take proactive steps to retain customers.
""")


if menu == "Home":
    st.header("Welcome to Home Page")
    
CreditScore = st.number_input("CreditScore")
Age = st.number_input("Age")
Balance = st.number_input("Balance")
IsActiveMember = st.selectbox("IsActiveMember",[0,1])
EstimatedSalary = st.number_input("EstimatedSalary")

Gender = st.selectbox("Gender",["Male","Female"])
Geography = st.selectbox("Geography",["France","Germany","Spain"])

col1, col2 = st.columns(2)

with col1:
    CreditScore = st.number_input("Credit Score")
    Age = st.number_input("Age")

with col2:
    Balance = st.number_input("Balance")
    IsActiveMember = st.selectbox("Active Member", [0,1])

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







