import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("employee_attrition.csv")
    return df

df = load_data()

# App Title
st.title("Employee Attrition Dashboard")

# Show Data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Attrition Count
st.subheader("Attrition Distribution")
fig, ax = plt.subplots()
sns.countplot(data=df, x="Attrition", palette="coolwarm", ax=ax)
st.pyplot(fig)

# Attrition by Department
st.subheader("Attrition by Department")
fig, ax = plt.subplots()
sns.countplot(data=df, x="Department", hue="Attrition", palette="coolwarm", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Salary vs Attrition
st.subheader("Monthly Income vs Attrition")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="Attrition", y="MonthlyIncome", palette="coolwarm", ax=ax)
st.pyplot(fig)

st.write("This dashboard helps analyze employee attrition patterns.")
