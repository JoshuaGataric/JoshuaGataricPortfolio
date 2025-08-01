import streamlit as st

# Custom CSS for dark theme
st.markdown(
    """
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    .stButton > button {
        background-color: #1E1E1E;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("Forecasting Traffic Volume Project")
st.image("Traffic.jpg")
st.header("Project Overview")

# Overview Section
st.write("""
This project utilizes Gaussian Process (GP) regression to predict hourly traffic volume on a Minneapolis highway. Using the Metro Interstate Traffic Volume dataset from the UCI Machine Learning Repository, I trained the model with data from 2016 to 2017 and validated it with 2018 data.

The goal was to forecast future traffic trends based on date and time information only. I experimented with different kernel functions to capture periodic traffic patterns (such as weekly cycles), and evaluated the models using performance metrics like RMSE and MAE. The best-performing model achieved a validation RMSE of 524.06, successfully identifying recurring trends in traffic volume.

For this project, I used only the Python libraries NumPy, SciPy.special, and Pandas to implement the Gaussian Process regression and kernel combinations.

Future work will explore incorporating weather and holiday data to enhance the model’s predictive accuracy, as well as investigating the integration of hybrid models that combine GPs with other time-series forecasting methods.
""")

# Results Section
st.subheader("Results")

# RBF results
st.write("### RBF Kernel Results:")
st.image("GP1.png", caption="Observed and predicted traffic volume for GP with RBF kernel (ℓ = 1)")

# RMSE results
st.write("### Root Mean Squared Error Model Evaluation:")
st.image("GP2.png", caption="Root Mean Squared Error (RMSE) by model for training and validation. Best models for each kernel by validation RMSE are shown. Sum Periodic 2 consists of a sum of 2 periodic kernels with periods of 7 days and 1 year. Sum periodic 3 consists of sum of 3 periodic kernels with periods of 24 hours, 7 days, and 1 year")

# Periodic results
st.write("### Periodic Kernel Results:")
st.image("GP4.png", caption="Observed and predicted traffic volume for GP with periodic kernel (ℓ = 0.01, p = 168) on 2 weeks of validation data (01/01/2018 to 01/01/2014)")
