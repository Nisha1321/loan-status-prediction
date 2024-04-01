import streamlit as st
import pandas as pd
import pickle

def show_entry():
    st.write("Please enter customer details:")
    gender = st.selectbox("Gender", ['Male', 'Female'])
    married = st.selectbox("Married", ['Yes', 'No'])
    dependents = st.select_slider("Dependents", options=[0, 1, 2, 3, 4])  
    education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
    applicant_income = st.number_input("Applicant Income", step=1)  
    coapplicant_income = st.number_input("Coapplicant Income")  
    loan_amount = st.number_input("Loan Amount")  
    loan_amount_term = st.number_input("Loan Amount Term")  
    credit_history = st.selectbox("Credit History", ['Yes', 'No'])  
    property_area = st.selectbox("Property Area", ['Urban', 'Semiurban', 'Rural'])
    
    
    gender = 1.0 if gender == 'Male' else 0.0
    married = 1.0 if married == 'Yes' else 0.0
    education = 1.0 if education == 'Graduate' else 0.0
    self_employed = 1.0 if self_employed == 'Yes' else 0.0
    credit_history = 1.0 if credit_history == 'Yes' else 0.0
    property_area_mapping = {'Urban': 0, 'Semiurban': 1, 'Rural': 2}
    property_area = property_area_mapping[property_area]
    with open('logistic.pkl','rb') as f:
         model = pickle.load(f)
    df = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })
    result = model.predict(df)
    
    if result[0] == 1:
        st.write("# Loan approved")
    else:
        st.write("# Loan not approved")

st.title("Loan Status Prediction Using Machine Learning")

show_entry()
