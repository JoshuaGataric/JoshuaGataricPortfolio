import streamlit as st

# Custom CSS for dark theme
st.markdown(
    """
    <style>
    body {
        background-color: #0E1117;  /* Dark background color */
        color: white;  /* Text color */
    }
    .stButton > button {
        background-color: #1E1E1E;  /* Button background color */
        color: white;  /* Button text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Select a page",
    ["Home","Hobbies", "Forecasting Traffic Volume","2025 March Madness","Wine Tasting Model Training", "NFL Combine Analysis","THE GAME Corpus Construction","2022 World Cup Analysis","Stadium Seat Booking System"]
)

# Navigation logic
if page == "Home":
    st.title("Joshua Gataric Portfolio")

    # Bio Section
    st.subheader("Bio")
    st.image("Header.jpeg", width=200)  # Ensure the image is in the same directory or provide the correct path
    st.write("""
    Hi! I'm Joshua Gataric, currently pursuing a Master of Data Science at UCI. I have a keen interest in machine learning, artificial intelligence, and exploratory data analysis.
    My role as a supplemental instruction leader at San Diego State ignited my curiosity and passion for statistics.
    Additionally, undergraduate coursework such as Ling 583 Statistical Methods in Text Analysis and STAT 410 R Programming and Data Science 
    has deepened my enthusiasm for the field of data science.
    """)

    # Education Section
    st.subheader("Education")
    st.write("""
    - M.S. Data Science - UC Irvine (Expected Graduation December 2025)
    - B.S. Statistics - San Diego State, Magna Cum Laude
    """)

    # Projects Section
    st.subheader("Projects")
    st.write("You can view the projects using the sidebar:")
    st.write("- Forecasting Traffic Volume")
    st.write("- 2025 March Madness")
    st.write("- Wine Tasting Model Training")
    st.write("- NFL Combine Analysis")
    st.write("- THE GAME Corpus Construction")
    st.write("- 2022 World Cup Analysis")
    st.write("- Stadium Seat Booking System")

    # Connect with Me Section
    st.subheader("Connect with Me")
    st.write("You can find me on LinkedIn:")
    st.write("[www.linkedin.com/in/joshua-gataric](https://www.linkedin.com/in/joshua-gataric)")

    # Footer
    st.write("© 2025 Joshua Gataric")

elif page == "Hobbies":
    exec(open("hobbies.py").read())

elif page == "Forecasting Traffic Volume":
    exec(open("FTV.py").read())

elif page == "2025 March Madness":
    exec(open("NCAAB.py").read())

elif page == "Wine Tasting Model Training":
    exec(open("wine_project.py").read())

elif page == "NFL Combine Analysis":
    exec(open("nfl_project.py").read())

elif page == "THE GAME Corpus Construction":
    exec(open("corpus_construction.py").read())

elif page == "2022 World Cup Analysis":
    exec(open("world_cup_analysis_project.py").read())

elif page == "Stadium Seat Booking System":
    exec(open("ticket_sales_database.py").read())
