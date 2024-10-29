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
st.title("2022 FIFA World Cup PCA Analysis")
st.image("WorldCupImage.jpg")  # Replace with an appropriate image file
st.header("Project Overview")

# Overview Section
st.write("""
This project analyzes player statistics from the 2022 FIFA World Cup, including goals, assists, successful dribbles, tackles, and more. I applied Principal Component Analysis (PCA) using SAS to capture the relationships betIen these stats and reveal underlying patterns in player and team performance.

PCA helped in identifying key components representing offensive versus defensive metrics, player experience, and age. This analysis gives insights into the characteristics of top players and teams, highlighting key differences betIen offensive and balanced play styles.
""")

# Results Section
st.subheader("Results")

# Display PCA Component Categorization
st.write("### PCA Categorization:")
st.image("PCA_Categorization.png", caption="Principal Component Assignment ")
st.write("""
Based on the retained components, PC1 represents an average across player statistics, with similar values across variables except Age. PC2 contrasts defensive and offensive metrics (positive for defense, negative for offense). PC3 primarily captures the influence of Age, indicating player experience, as shown by its unique high value for this variable. A similar pattern emerged when analyzing by team.
""")


# Display PC1 vs PC2 results
st.write("### PC1 vs PC2 Analysis:")
st.image("PC1vsPC2.png", caption="PC1 vs PC2 for Teams and Players")

st.write("""
In this analysis, top players like Messi and Mbappe stand out with high offensive statistics. Among teams, Argentina and Croatia show a balanced approach, while France leans more offensively.
""")

# Display PC2 vs PC3 results
st.write("### PC2 vs PC3 Analysis:")
st.image("PC2vsPC3.png", caption="PC2 vs PC3 for Teams and Players")
st.write("""
This analysis highlights the influence of age. Young players like Musiala and Bellingham appear, with Ecuador identified as the youngest team and Brazil the oldest.
""")

# Display PC1 vs PC3 results
st.write("### PC1 vs PC3 Analysis:")
st.image("PC1vsPC3.png", caption="PC1 vs PC3 for Teams and Players")
st.write("""
The PC1 vs PC3 plot shows experience-related trends. Although top teams like Croatia, Argentina, and France have high overall performance, Croatia has a younger average age compared to the others.
""")

# Footer
st.write("© 2024 Joshua Gataric")
