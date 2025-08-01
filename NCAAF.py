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
st.title("2024-2025 College Football MANOVA Analysis")
st.image("NCAAF.png")
st.header("Project Overview")

# Overview Section
st.write(""" This project compares the performance of four MANOVA tests—Wilks’ Lambda, Pillai’s Trace, Lawley-Hotelling Trace, and Roy’s Largest Root—through simulations and NCAA football data from the 2024–2025 season. Simulations assessed Type I error and power under varying sample sizes and covariance structures. Wilks, Pillai, and Lawley-Hotelling maintained nominal error rates, while Roy’s test showed higher power but inflated false positives. Real-world analysis revealed significant conference-level differences in passing stats (p < 0.001) but no differences in rushing performance. R packages used include tidyverse, dplyr, tidyr, ggplot2, MASS, and knitr. Future work could extend this analysis to other sports or test robustness under non-normal data assumptions.
""")

# Simulation Results Section
st.subheader("Simulation Results")

# Power results
st.write("### Power Tables:")
st.image("NCAAF1.png", caption="Results are based on four scenarios: Independent and Equal Variance, Positively Dependent, Negatively Dependent, Independent and Unequal Variance")

# Type I error results
st.write("### Type I Error Tables:")
st.image("NCAAF2.png", caption="Results are based on four scenarios: Independent and Equal Variance, Positively Dependent, Negatively Dependent, Independent and Unequal Variance")

# Real DataResults Section
st.subheader("Real Data Results")

# Passing EDA results
st.write("### Passing Exploratory Data Analysis:")
st.image("NCAAF3.png", caption="Results are broken up into four categories: Avg Passing Yards by Conference, Avg Passing Touchdowns by Conference, Avg Pass Attempts by Conference, and Avg Pass Completions by Conference ")

# Rushing  EDA results
st.write("### Rushing Exploratory Data Analysis:")
st.image("NCAAF4.png")
st.image("NCAAF5.png", caption="Results are broken up into three categories: Avg Rushing Yards per Attempt by Conference, Avg Rushing Yards per Game by Conference, and Avg Rushing Attempts per Player by Conference ")

# MANOVA Test Results
st.write("### MANOVA Test Results:")
st.image("NCAAF6.png", caption = "Test Results indicate a significant difference in passing stats between conferences but do not show a significant difference in rushing stats ")

# Footer
st.write("© 2025 Joshua Gataric")
