import streamlit as st
import pickle
import pandas as pd
import joblib
xgb_model = joblib.load("xgboost_model.pkl")
st.title("Fraud Detection App")
amount = st.number_input("Transaction Amount", min_value=0.0, step=0.01)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, step=0.01)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, step=0.01)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, step=0.01)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, step=0.01)
balance_org = st.number_input("Balance Org", min_value=0.0, step=0.01)
balance_dest = st.number_input("Balance Dest", min_value=0.0, step=0.01)
type_choice = st.selectbox("Transaction Type", options=["CASH_IN", "CASH_OUT", "TRANSFER", "PAYMENT", "DEBIT"])

if st.button("Predict Fraud"):
    input_data = pd.DataFrame([{
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "balance_org": balance_org,
        "balance_dest": balance_dest,
        "type": type_choice
    }])
    xgb_pred = xgb_model.predict(input_data)[0]

    st.write(f"**Logistic Regression:** {'Fraud' if log_pred==1 else 'Not Fraud'}")

    st.write(f"**XGBoost:** {'Fraud' if xgb_pred==1 else 'Not Fraud'}")
