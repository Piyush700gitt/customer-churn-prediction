# Customer Churn Prediction using Machine Learning

A machine learning project that predicts whether a telecom customer is likely to churn based on demographic, service usage, and account-related information.

## 🚀 Live Demo

👉 [Try the Customer Churn Prediction App](https://customer-churn-prediction-sgm3ztcf8tuxsoijnyeupb.streamlit.app/)


## 📌 Project Overview

Customer churn refers to customers leaving or cancelling a company's services.

The goal of this project is to build a machine learning system that can:

- Analyze customer information and service usage
- Identify factors associated with customer churn
- Predict the probability of customer churn
- Classify customers into different churn-risk levels
- Provide actionable retention recommendations

The project also includes an interactive Streamlit web application for real-time predictions.

---

## 🎯 Business Problem

Telecom companies lose revenue when customers leave their services.

Instead of waiting for customers to churn, the company can use machine learning to identify customers who are at higher risk of leaving.

This allows the company to take preventive actions such as:

- Personalized offers
- Customer support follow-ups
- Better service plans
- Retention campaigns

---

## 📂 Dataset

The project uses the **Telco Customer Churn** dataset.

The dataset contains customer demographic information, services, contract details, billing information, and churn status.

### Target Variable

`Churn`

- `Yes` → Customer churned
- `No` → Customer stayed

### Main Features

- Gender
- SeniorCitizen
- Partner
- Dependents
- Tenure
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

### Engineered Features

Two additional features were created during feature engineering:

- `TotalServices` — Total number of subscribed services
- `TenureGroup` — Customer tenure grouped into New, Early, Medium, and Long-term

---

## 🔍 Exploratory Data Analysis

The project includes analysis of:

- Churn distribution
- Numerical feature distributions
- Categorical feature distributions
- Churn rate by contract type
- Churn rate by internet service
- Churn rate by payment method
- Churn rate by technical support
- Churn rate by senior citizen status
- Correlation analysis

### Key Insights

- Month-to-month customers have a significantly higher churn rate.
- Customers with shorter tenure are more likely to churn.
- Fiber optic customers show relatively higher churn.
- Electronic check users show relatively higher churn.
- Customers without technical support show higher churn.
- Customers using fewer services tend to have higher churn risk.

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

1. Checked for missing values
2. Checked for duplicate records
3. Converted `TotalCharges` from object to numeric
4. Handled missing `TotalCharges` values
5. Removed the unique `customerID` column
6. Performed feature engineering
7. Split data into training and testing sets
8. Applied median imputation to numerical features
9. Applied most-frequent imputation to categorical features
10. Standardized numerical features
11. Applied One-Hot Encoding to categorical features

---

## 🤖 Machine Learning Models

Three classification algorithms were implemented and compared:

### 1. Logistic Regression

Used as a baseline classification model.

### 2. Random Forest

An ensemble tree-based model capable of capturing nonlinear relationships.

### 3. Gradient Boosting

An ensemble boosting algorithm that sequentially improves weak learners.

---

## 📊 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

Since customer churn is a business-risk problem, **Recall, F1-Score, and ROC-AUC** were considered along with accuracy.

### Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 79.25% | 63.14% | 52.67% | 57.43% | 83.50% |
| Random Forest | 78.18% | 61.36% | 48.40% | 54.11% | 81.47% |
| **Gradient Boosting** | **79.53%** | **63.87%** | **52.94%** | **57.89%** | **83.91%** |

### Model Selection

**Gradient Boosting Classifier** was selected as the final model because it achieved the best overall performance, including the highest **F1-Score (57.89%)** and **ROC-AUC (83.91%)** among the evaluated models.

## 🌐 Streamlit Application

The project includes an interactive Streamlit application.

The application allows users to enter customer information and receive:

- Churn prediction
- Churn probability
- Risk level
- Recommended business action

### Risk Levels

| Churn Probability | Risk Level |
|---|---|
| < 30% | Low Risk |
| 30% – 59% | Medium Risk |
| ≥ 60% | High Risk |

---

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   └── churn_model.joblib
│
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
├── src/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
