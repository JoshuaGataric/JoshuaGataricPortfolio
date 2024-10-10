import streamlit as st

# Header
st.title("Joshua Gataric Portfolio")
st.header("Welcome to My Interactive Portfolio")

# Bio Section
st.subheader("Bio")
st.image("Header.jpeg", width=200)  # Make sure you have the image in the same directory
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
st.write("- [Wine Tasting Model Training Project](https://joshuagataric.github.io/Wine-Tasting-Model-Training-Project)")
st.write("- [NFL Combine Analysis](https://joshuagataric.github.io/NFL-Combine-Analysis)")

# Connect with Me Section
st.subheader("Connect with Me")
st.write("You can find me on LinkedIn:")
st.write("[www.linkedin.com/in/joshua-gataric](https://www.linkedin.com/in/joshua-gataric)")

# Footer
st.write("© 2024 Joshua Gataric")
