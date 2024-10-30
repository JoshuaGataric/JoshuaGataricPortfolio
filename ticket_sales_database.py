import streamlit as st

# Set up the page title and introduction
st.title("Stadium Seat Booking System")

# Introduction Section
st.header("Project Overview")
st.write("""
For this project, I developed a system that manages seat allocation for various events. It ensures an efficient and accurate experience for users booking seats for events held at stadiums, concert venues, theaters, and more.
""")

# Conceptual Data Modeling and Database Design
st.header("Conceptual Data Modeling and Database Design")
st.image("ERDiagram.png", caption="ER Diagram for Seat Booking System")
st.image("RelationModel.png", caption="Schema Design")

# Database Implementation Section with SQL Code
st.header("Database Implementation")

st.subheader("Example Table: Users")
st.write("The `Users` table stores basic user details, ensuring each user's unique identity in the system.")
st.code("""
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Username VARCHAR(160) NOT NULL,
    Password VARCHAR(160) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    PRIMARY KEY (UserID)
);
""", language="sql")

st.subheader("Example Data Insertion")
st.write("Here’s an example of inserting user information into the `Users` table.")
st.code("""
INSERT INTO Users (Username, Password, Email) VALUES
('Alice123', 'password123', 'alice@example.com'),
('Bob234', 'password234', 'bob@example.com');
""", language="sql")

# Dashboard and Results Section
st.header("Dashboard")
st.write("Here are some example visualizations I created using sample data in this project.")
st.image("Dashboard1.png", caption="Dashboard Example 1")
st.image("Dashboard2.png", caption="Dashboard Example 2")
st.image("Dashboard3.png", caption="Dashboard Example 3")
