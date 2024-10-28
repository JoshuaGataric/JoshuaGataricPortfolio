import streamlit as st

# Overview Section
st.write("""
This project analyzed media outlet reactions to Michigan’s 30-24 victory over Ohio State last season, emphasizing linguistic trends that shape narratives around high-stakes sports rivalries. By building a custom corpus with articles from ESPN, FOX SPORTS, and CBS SPORTS, I explored recurring patterns in language through collocation analysis, highlighting the cultural intensity and significance of "THE GAME."

Using bigram and trigram collocations along with measures like raw frequency, PMI, and likelihood ratio, this project unveils key players, coaches, and themes from the media’s perspective. The outcome not only reveals shared terminology but also paints a picture of how language encapsulates rivalry in collegiate sports.
""")

# Results Section
st.subheader("Results")

# Display Raw Frequency Analysis
st.write("### Raw Frequency Collocations:")
st.image("RawFrequencyCollocations.png", caption="Raw Frequency Bigrams/Trigrams")

# Display PMI Analysis
st.write("### PMI Collocations:")
st.image("PMICollocations.png", caption="PMI Bigrams/Trigrams")

# Display Likelihood Ratio Analysis
st.write("### Likelihood Ratio Collocations:")
st.image("LikelihoodRatioCollocations.png", caption="Likelihood Ratio Bigrams/Trigrams")

# Footer
st.write("© 2024 Joshua Gataric")
