import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Employee Attrition Prediction App")

# Form for user input
with st.form("attrition_form"):
    Age = st.number_input("Age", min_value=18, max_value=65, step=1)
    BusinessTravel = st.selectbox("Business Travel", ['Rarely', 'Frequently', 'No Travel'])
    DailyRate = st.number_input("Daily Rate", min_value=0)
    Department = st.selectbox("Department", ['Sales', 'Research & Development', 'Human Resources'])
    DistanceFromHome = st.number_input("Distance From Home", min_value=0)
    Education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
    EducationField = st.selectbox("Education Field", ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources', 'Other'])
    EnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
    Gender = st.selectbox("Gender", ['Male', 'Female'])
    HourlyRate = st.number_input("Hourly Rate", min_value=0)
    JobInvolvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
    JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    JobRole = st.selectbox("Job Role", ['Laboratory Technician', 'Sales Executive', 'Research Scientist', 'Manager', 'Manufacturing Director', 'Healthcare Representative', 'Research Director', 'Human Resources', 'Sales Representative'])
    JobSatisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
    MaritalStatus = st.selectbox("Marital Status", ['Married', 'Single', 'Divorced'])
    MonthlyIncome = st.number_input("Monthly Income", min_value=0)
    NumCompaniesWorked = st.number_input("Number of Companies Worked In", min_value=0)
    OverTime = st.selectbox("Over Time", ['Yes', 'No'])
    PerformanceRating = st.selectbox("Performance Rating", [1, 2, 3, 4])
    RelationshipSatisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
    StockOptionLevel = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    TotalWorkingYears = st.number_input("Total Working Years", min_value=0)
    TrainingTimesLastYear = st.selectbox("Training Times Last Year", [0, 1, 2, 3, 4, 5, 6])
    WorkLifeBalance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
    YearsAtCompany = st.number_input("Years At Company", min_value=0)
    YearsInCurrentRole = st.number_input("Years In Current Role", min_value=0)
    YearsSinceLastPromotion = st.number_input("Years Since Last Promotion", min_value=0)
    YearsWithCurrManager = st.number_input("Years With Curr Manager", min_value=0)

    submitted = st.form_submit_button("Predict")

# If form is submitted
if submitted:
    data = {
        'Age': int(Age),
        'BusinessTravel': BusinessTravel,
        'DailyRate': int(DailyRate),
        'Department': Department,
        'DistanceFromHome': int(DistanceFromHome),
        'Education': Education,
        'EducationField': EducationField,
        'EnvironmentSatisfaction': int(EnvironmentSatisfaction),
        'Gender': Gender,
        'HourlyRate': int(HourlyRate),
        'JobInvolvement': int(JobInvolvement),
        'JobLevel': int(JobLevel),
        'JobRole': JobRole,
        'JobSatisfaction': int(JobSatisfaction),
        'MaritalStatus': MaritalStatus,
        'MonthlyIncome': int(MonthlyIncome),
        'NumCompaniesWorked': int(NumCompaniesWorked),
        'OverTime': OverTime,
        'PerformanceRating': int(PerformanceRating),
        'RelationshipSatisfaction': int(RelationshipSatisfaction),
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': int(TotalWorkingYears),
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': int(WorkLifeBalance),
        'YearsAtCompany': int(YearsAtCompany),
        'YearsInCurrentRole': int(YearsInCurrentRole),
        'YearsSinceLastPromotion': int(YearsSinceLastPromotion),
        'YearsWithCurrManager': int(YearsWithCurrManager)
    }

    df = pd.DataFrame([data])

    ### --- Transformation Logic ---
    # (Same processing logic from your original Flask app)
    # You can modularize this into a function if needed.
    # For brevity, you can put your transformation code here...
    # === Insert feature engineering & encoding section ===
    # (copy from your Flask code between dict -> df -> prediction)

    # Final prediction
    prediction = model.predict(df)

    if prediction[0] == 0:
        st.success("✅ Employee Might NOT Leave The Job")
    else:
        st.error("⚠️ Employee Might Leave The Job")
