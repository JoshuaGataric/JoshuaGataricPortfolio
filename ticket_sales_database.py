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

st.subheader("Users Table")
st.code("""
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Username VARCHAR(160) NOT NULL,
    Password VARCHAR(160) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    PRIMARY KEY (UserID)
);
""", language="sql")

st.subheader("Venues Table")
st.code("""
CREATE TABLE Venues (
    VenueID INT AUTO_INCREMENT,
    Name VARCHAR(160) NOT NULL,
    Capacity INT NOT NULL,
    Address VARCHAR(255) NOT NULL,
    PRIMARY KEY (VenueID)
);
""", language="sql")

st.subheader("Events Table")
st.code("""
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT,
    VenueID INT NOT NULL,
    Name VARCHAR(160) NOT NULL,
    EventDate DATE NOT NULL,
    EventTime TIME,
    PRIMARY KEY (EventID),
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID)
);
""", language="sql")

st.subheader("Seats Table")
st.code("""
CREATE TABLE Seats (
    SeatID INT AUTO_INCREMENT,
    VenueID INT NOT NULL,
    Section VARCHAR(50) NOT NULL,
    SeatRow INT NOT NULL,
    Number INT NOT NULL,
    Price DECIMAL(10,2),
    PRIMARY KEY (SeatID),
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID),
    UNIQUE KEY (VenueID, Section, SeatRow, Number)
);
""", language="sql")

st.subheader("Bookings Table")
st.code("""
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    UserID INT NOT NULL,
    EventID INT NOT NULL,
    SeatID INT NOT NULL,
    BookingDate DATE NOT NULL,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (SeatID) REFERENCES Seats(SeatID),
    UNIQUE KEY (EventID, SeatID)
);
""", language="sql")

st.subheader("Transactions Table")
st.code("""
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT,
    BookingID INT NOT NULL,
    Amount DECIMAL(10,2),
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PaymentMethod VARCHAR(50),
    PRIMARY KEY (TransactionID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);
""", language="sql")

# Dummy Data Section
st.header("Dummy Data")
st.subheader("Inserting Data into Users")
st.code("""
INSERT INTO Users (Username, Password, Email) VALUES
('Alice123', 'password123', 'alice@example.com'),
('Bob234', 'password234', 'bob@example.com');
""", language="sql")

st.subheader("Inserting Data into Venues")
st.code("""
INSERT INTO Venues (Name, Capacity, Address) VALUES
('Stadium A', 20000, '123 Venue Road, CityA'),
('Arena B', 15000, '234 Venue Street, CityB');
""", language="sql")

# Repeat for other tables as necessary

# Dashboard and Results Section
st.header("Dashboard")
st.write("Here are some example visualizations I created using sample data in this project.")
st.image("Dashboard1.png", caption="Dashboard Example 1")
st.image("Dashboard2.png", caption="Dashboard Example 2")
st.image("Dashboard3.png", caption="Dashboard Example 3")
