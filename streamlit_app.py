import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Streamlit page config
st.set_page_config(page_title="Random Forest Feature Importance", layout="wide")

# Title and description
st.title("Random Forest Feature Importance Visualization")
st.markdown("""
    Upload your dataset (CSV) and let the model calculate the feature importance using Random Forest.
    The feature importance will be displayed in a scatter plot.
""")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    # Load data into a pandas DataFrame
    df = pd.read_csv("Employee-Attrition.csv")
    
    # Show the first few rows of the dataset
    st.write("Dataset Preview:", df.head())

    # Select the target column for the classification task (modify as per your dataset)
    target_column = st.selectbox("Select the target column:", df.columns)

    # Select features for training
    feature_columns = [col for col in df.columns if col != target_column]

    # Split data into features (X) and target (y)
    X = df[feature_columns]
    y = df[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train Random Forest model
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # Get feature importances
    feature_importances = rf.feature_importances_

    # Plot the feature importance using Plotly
    trace = go.Scatter(
        y=feature_importances,
        x=feature_columns,
        mode='markers',
        marker=dict(
            sizemode='diameter',
            sizeref=1,
            size=13,
            color=feature_importances,
            colorscale='Portland',
            showscale=True
        ),
        text=feature_columns
    )

    data = [trace]

    layout = go.Layout(
        autosize=True,
        title='Random Forest Feature Importance',
        hovermode='closest',
        xaxis=dict(
            ticklen=5,
            showgrid=False,
            zeroline=False,
            showline=False
        ),
        yaxis=dict(
            title='Feature Importance',
            showgrid=False,
            zeroline=False,
            ticklen=5,
            gridwidth=2
        ),
        showlegend=False
    )

    fig = go.Figure(data=data, layout=layout)

    # Display the plot in Streamlit
    st.plotly_chart(fig)

else:
    st.warning("Please upload a CSV file to proceed.")
