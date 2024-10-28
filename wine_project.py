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
st.title("Wine Tasting Model Training Project")
st.image("Wine.jpg")
st.header("Project Overview")

# Overview Section
st.write("""
This project demonstrated the application of machine learning techniques to predict wine labels based on wine reviews. By leveraging text processing tools such as CountVectorizer and TfidfVectorizer, and employing models like LinearSVC and RandomForestClassifier, the project achieved meaningful insights into wine label prediction.

The use of F1 macro average scores provided a balanced evaluation of the model’s precision and recall across different labels, while the confusion matrix visualization offered a deeper understanding of model performance and areas for improvement.

Future work could involve exploring deeper models like neural networks or incorporating more features from the wine reviews, such as reviewer characteristics or wine-specific attributes like price and region, to further enhance predictive performance.
""")

# Results Section
st.subheader("Results")

# Display Linear SVC results
st.write("### Linear SVC Confusion Matrix and F1 Macro Avg Score:")
st.image("SVMConfusionMatrix.png", caption="Linear SVC Confusion Matrix")
st.image("SVMScores.png", caption="Linear SVC F1 Macro Avg Score")

# Display Random Forest results
st.write("### Random Forest Confusion Matrix and F1 Macro Avg Score:")
st.image("RandomForestConfusionMatrix.png", caption="Random Forest Confusion Matrix")
st.image("RandomForestScores.png", caption="Random Forest F1 Macro Avg Score")

# Footer
st.write("© 2024 Joshua Gataric")
