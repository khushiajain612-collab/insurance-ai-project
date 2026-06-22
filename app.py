import streamlit as st

st.title("Life Insurance Risk Analysis & Advisory Agent")

st.header("Personal Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married"]
)

dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10
)

st.header("Financial Information")

annual_income = st.number_input(
    "Annual Income (₹)"
)

outstanding_loans = st.number_input(
    "Outstanding Loans (₹)"
)

existing_cover = st.number_input(
    "Existing Life Insurance Cover (₹)"
)

st.header("Health Information")

smoker = st.radio(
    "Do you smoke?",
    ["No", "Yes"]
)

medical_conditions = st.multiselect(
    "Medical Conditions",
    [
        "Diabetes",
        "Hypertension",
        "Heart Disease",
        "Respiratory Disease",
        "Cancer History"
    ]
)

st.header("Insurance Goal")

goal = st.selectbox(
    "Primary Goal",
    [
        "Family Protection",
        "Loan Protection",
        "Wealth Protection",
        "Retirement Planning"
    ]
)

if st.button("Generate Recommendation"):

    mortality_score = 20

    if age > 50:
        mortality_score += 20

    if smoker == "Yes":
        mortality_score += 25

    mortality_score += len(medical_conditions) * 10

    recommended_coverage = (
        annual_income * 10
        + outstanding_loans
        - existing_cover
    )

    if recommended_coverage < 500000:
        recommended_coverage = 500000

    if annual_income >= 1500000:
        product = "Premium Protect"

    elif annual_income >= 500000:
        product = "Secure Term Plus"

    else:
        product = "Essential Term"

    st.success("Recommendation Generated")

    st.subheader("Mortality Score")
    st.write(mortality_score)

    st.subheader("Recommended Coverage")
    st.write(f"₹{recommended_coverage:,.0f}")

    st.subheader("Recommended Product")
    st.write(product)