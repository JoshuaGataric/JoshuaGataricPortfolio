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
st.title("2025 March Madness Prediction Project")
st.image("NCAAB.jpg")
st.header("Project Overview")

# Overview Section
st.write("""
This project focuses on forecasting the outcomes of the 2025 NCAA Division I Men’s and Women’s Basketball Tournaments by predicting the results of every possible matchup. Using historical NCAA game data, I built multiple predictive models to estimate the probability of a team winning a given game, with performance evaluated using the Brier score, a widely used metric for probabilistic forecasts.

The models developed include:
Logistic Regression,Random Forest,XGBoost,Multi-Layer Perceptron (MLP)

These were implemented using Python libraries:
Pandas, NumPy, Scikit-learn, Torch, and XGBoost

The project was created as an entry into the official 2025 NCAA Tournament Forecasting Challenge, where participants compete for points, medals, prizes, and basketball glory. Beyond the competition, this work demonstrates the power of data-driven modeling in sports analytics, providing insights into how different machine learning approaches handle high-stakes, bracket-based tournament predictions.

Future work includes incorporating real-time player statistics, seed-based tournament path modeling, and experimenting with Bayesian models for uncertainty estimation.
""")

# Results Section
st.subheader("Results")

# Brier results
st.write("### Brier Results:")
st.image("NCAAB1.png", caption="XGBoost is the best model in regards to this metric")

# Log Loss results
st.write("### Log Loss Results:")
st.image("NCAAB2.png", caption="XGBoost and Random Forest are tied for best model in regards to this metric")

# MAE results
st.write("### Mean Absolute Error Results:")
st.image("NCAAB3.png", caption="XGBoost and Random Forest are tied for best model in regards to this metric")

# MSE results
st.write("### Cross-Validated Mean Squared Error Results:")
st.image("NCAAB4.png", caption="MLP is the best model in regards to this metric")

# Footer
st.write("© 2026 Joshua Gataric")
