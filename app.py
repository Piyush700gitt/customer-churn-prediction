import streamlit as st
import pandas as pd
import joblib

from src.utils import (
    calculate_total_services,
    get_tenure_group,
    get_risk_level
)


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load("models/churn_model.joblib")


model = load_model()
with st.sidebar:
    st.header("📌 About the Model")

    st.write(
        "This application predicts whether a customer "
        "is likely to churn based on demographic, service, "
        "and account-related information."
    )

    st.divider()

    st.subheader("🤖 Model")
    st.write("Gradient Boosting Classifier")

    st.subheader("📊 Evaluation")
    st.write("Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC")

    st.divider()

    st.caption("Customer Churn Prediction • Machine Learning Project")
st.title("📊 Customer Churn Prediction")
st.caption(
    "Predict customer churn using demographic, service, and account information."
)
st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=72,
        value=12
    )

with col2:
    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )
    col1, col2 = st.columns(2)

with col1:
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=150.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )
st.divider()
    

if st.button(
    "Predict Churn",
    use_container_width=True
):

    total_services = calculate_total_services(
        phone_service,
        multiple_lines,
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies
    )

    tenure_group = get_tenure_group(tenure)

    customer_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior_citizen],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "TotalServices": [total_services],
        "TenureGroup": [tenure_group]
    })

    prediction = model.predict(customer_data)[0]
    probability = model.predict_proba(customer_data)[0][1]

    st.divider()
    st.subheader("Prediction Result")

    if prediction == "Yes":
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    if probability < 0.30:
        risk_message = (
            "Customer has a relatively low probability of churn."
        )
    elif probability < 0.60:
        risk_message = (
            "Customer shows a moderate risk of churn."
        )
    else:
        risk_message = (
            "Customer has a high probability of churn."
        )

    risk_level = get_risk_level(probability)

    if probability < 0.30:
        st.success("🟢 Low Churn Probability")
    elif probability < 0.60:
        st.warning("🟡 Medium Churn Probability")
    else:
        st.error("🔴 High Churn Probability")

    st.subheader(f"Risk Level: {risk_level}")
    st.info(risk_message)

    # Business Recommendation
    st.subheader("Recommended Action")

    if probability < 0.30:
        recommendation = (
            "No immediate retention action required. "
            "Continue regular customer engagement."
        )

    elif probability < 0.60:
        recommendation = (
            "Consider targeted engagement, personalized offers, "
            "or customer support follow-up."
        )

    else:
        recommendation = (
            "Prioritize this customer for retention outreach "
            "and consider offering incentives or special plans."
        )

    st.write(recommendation)

    st.progress(float(probability))

    st.caption(
        f"Estimated probability of churn: {probability:.1%}"
    )