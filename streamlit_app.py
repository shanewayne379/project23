import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.tools as tls
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss, classification_report
from imblearn.over_sampling import SMOTE
import xgboost as xgb

# Load dataset
st.title("Employee Attrition Analysis")
attrition = pd.read_csv('Employee-Attrition.csv')

# Display dataset
if st.checkbox("Show Raw Data"):
    st.write(attrition.head())

# KDE Plot
st.subheader("Age vs Total Working Years KDE Plot")
f, ax = plt.subplots(figsize=(8, 6))
sns.kdeplot(x=attrition['Age'], y=attrition['TotalWorkingYears'], shade=True, ax=ax)
st.pyplot(f)

# Placeholder for ML Model Training
st.subheader("Train a Machine Learning Model")
if st.button("Train Model"):
    X = attrition.drop(columns=['Attrition'])
    y = attrition['Attrition']
    smote = SMOTE()
    X_res, y_res = smote.fit_resample(X, y)
    model = RandomForestClassifier()
    model.fit(X_res, y_res)
    st.success("Model Trained Successfully!")
