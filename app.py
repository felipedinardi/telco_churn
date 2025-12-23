import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(page_title="Churn Prediction Tool", page_icon="🔮", layout="centered")

st.title("🔮 Churn Prediction Simulator")
st.markdown("Fill in the customer data below to check the cancellation probability.")

# 1. Load the trained model
if os.path.exists('churn_model.pkl'):
    model = joblib.load('churn_model.pkl')
else:
    st.error("File 'churn_model.pkl' not found! Please ensure the model file is in the same folder.")
    st.stop()

# --- INPUT INTERFACE ---
st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
    contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
    paperless = st.selectbox("Paperless Billing?", ['Yes', 'No'])
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.0)

with col2:
    payment_method = st.selectbox("Payment Method", [
        'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
    ])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security?", ['Yes', 'No'])
    tech_support = st.selectbox("Tech Support?", ['Yes', 'No'])

# Total Charges calculation
total_charges = tenure * monthly_charges

# Secondary fields in an expander to keep the UI clean
with st.expander("More Details (Demographics & Other Services)"):
    col_a, col_b = st.columns(2)
    with col_a:
        gender = st.selectbox("Gender", ['Female', 'Male'])
        senior = st.selectbox("Senior Citizen?", [0, 1])
        partner = st.selectbox("Partner?", ['Yes', 'No'])
        dependents = st.selectbox("Dependents?", ['Yes', 'No'])
    with col_b:
        phone = st.selectbox("Phone Service?", ['Yes', 'No'])
        multiple_lines = st.selectbox("Multiple Lines?", ['Yes', 'No'])
        online_backup = st.selectbox("Online Backup?", ['Yes', 'No'])
        device_protection = st.selectbox("Device Protection?", ['Yes', 'No'])
        streaming_tv = st.selectbox("Streaming TV?", ['Yes', 'No'])
        streaming_movies = st.selectbox("Streaming Movies?", ['Yes', 'No'])

# --- DATAFRAME CONSTRUCTION ---
# We include 'customerID' with a dummy value to avoid the ValueError
input_data = pd.DataFrame({
    'customerID': ['0000-AAAA'], 
    'gender': [gender], 
    'SeniorCitizen': [senior], 
    'Partner': [partner], 
    'Dependents': [dependents], 
    'tenure': [tenure], 
    'PhoneService': [phone],
    'MultipleLines': [multiple_lines], 
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security], 
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection], 
    'TechSupport': [tech_support], 
    'StreamingTV': [streaming_tv], 
    'StreamingMovies': [streaming_movies],
    'Contract': [contract], 
    'PaperlessBilling': [paperless],
    'PaymentMethod': [payment_method], 
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})

# --- PREDICTION LOGIC ---
st.divider()
if st.button('🚀 Analyze Churn Risk', use_container_width=True):
    try:
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] 

        # Show Results
        if prediction == 1:
            st.error(f"⚠️ **HIGH CHURN RISK**")
            st.metric("Cancellation Probability", f"{probability:.2%}")
            st.warning("Action recommended: Contact this customer with a loyalty offer.")
        else:
            st.success(f"✅ **LOW CHURN RISK**")
            st.metric("Cancellation Probability", f"{probability:.2%}")
            st.info("This customer is likely to stay.")
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.info("Tip: Make sure the model columns match the input data exactly.")