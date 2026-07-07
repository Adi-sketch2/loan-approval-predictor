import streamlit as st
import pickle 

model=pickle.load(open("random.pkl","rb"))

st.title("Loan Approval Prediction")
st.caption("This app predicts whether a loan will be approved or not based on the applicant's information.")

st.info(
    "This is a demo model trained on a specific Kaggle dataset. "
    "For the most reliable predictions, please enter values within these ranges:\n\n"
    "- Income (annual): ₹2,00,000 - ₹99,00,000\n"
    "- Loan amount: ₹3,00,000 - ₹3,95,00,000\n"
    "- Loan term: 2 - 20 years\n"
    "- CIBIL score: 300 - 900\n"
    "- Number of dependents: 0 - 5\n"
    "- Residential assets value: ₹0 - ₹2,91,00,000\n"
    "- Commercial assets value: ₹0 - ₹1,94,00,000\n"
    "- Luxury assets value: ₹3,00,000 - ₹3,92,00,000\n"
    "- Bank assets value: ₹0 - ₹1,47,00,000\n\n"
    "Values outside these ranges may lead to unreliable predictions, "
    "since the model has not been trained on such cases."
)

loan_amount=st.number_input("Enter the loan amount:",min_value=300000,max_value=39500000,value=15000000)

loan_term=st.number_input("Enter the loan term in years:",min_value=2, max_value=20, value=11)
credit_score=st.number_input("Enter the applicant's credit score:", min_value=300, max_value=900, value=600)

employment_status=st.radio("self employed:", ("yes", "no"))
if employment_status=="yes":
    employment_status=1
else:
    employment_status=0

education=st.radio("Education level:", ("graduate", "not graduate"))
if education=="graduate":
    education=1
else:
    education=0

dependents=st.number_input("Number of dependents:", min_value=0, max_value=5, value=2)
income=st.number_input("Enter the applicant's income:", min_value=200000,max_value=9900000,value=5000000)
residential_asset=st.number_input("Enter the value of residential assets:", min_value=0,max_value=29100000,value=7500000)
commercial_asset=st.number_input("Enter the value of commercial assets:", min_value=0,max_value=19400000,value=5000000)
luxury_asset=st.number_input("Enter the value of luxury assets:", min_value=300000,max_value=39200000,value=15000000)
bank_assets=st.number_input("Enter the value of bank assets:", min_value=0,max_value=14700000,value=5000000)

if st.button("Predict"):
    input_data=[dependents,education,employment_status,income,loan_amount,loan_term,credit_score,residential_asset,commercial_asset,luxury_asset,bank_assets]
    prediction=model.predict([input_data])
    if prediction[0]==1:
        st.success("The loan will be approved.")
    else:
        st.error("The loan will not be approved.")