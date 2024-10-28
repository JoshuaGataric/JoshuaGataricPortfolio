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
st.title("NFL Combine Analysis")
st.image("Combine.png")
st.header("Project Overview")

# Overview Section
st.write("""
This NFL Combine analysis provided a comprehensive statistical comparison of performance metrics across different player positions. By utilizing R packages such as tidyverse, dplyr, car, and rstatix, the project effectively identified and visualized key differences between player positions using scatter plots, boxplots, and pairwise t-tests.

The findings underscore the distinct physical profiles required for each position, with specific attributes like speed, strength, and explosiveness varying significantly across different roles on the field.

Future work could explore more advanced statistical models or delve into the relationship between Combine performance and long-term success in the NFL, offering a predictive view of how Combine metrics translate to professional performance.
""")

# Results Section
st.subheader("Results")

# Display NFL Combine results
st.write("### Weight vs Combine 40 Yard Dash Time by Position:")
st.image("WeightvsCombine40YardDashTimebyPosition.png", caption="Weight vs Combine 40 Yard Dash Time by Position")

st.write("### Height vs Combine 40 Yard Dash Time by Position:")
st.image("HeightvsCombine40YardDashTimebyPosition.png", caption="Height vs Combine 40 Yard Dash Time by Position")

st.write("### Boxplot of Combine 40 Yard Dash Time by Position:")
st.image("BoxplotofCombine40YardDashTimebyPosition.png", caption="Boxplot of Combine 40 Yard Dash Time by Position")

st.write("### Games-Howell Test:")
st.image("Games-HowellNFLCombine.png", caption="Games-Howell NFL Combine")

# Footer
st.write("© 2024 Joshua Gataric")
