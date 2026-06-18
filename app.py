import streamlit as st
import pickle

from feature_extractor import extract_features

# Page settings
st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #4CAF50;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 2rem;
}

.result-safe {
    background-color: #d4edda;
    color: #155724;
    padding: 15px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
}

.result-danger {
    background-color: #f8d7da;
    color: #721c24;
    padding: 15px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("phishing_url_model.pkl", "rb"))

# Header
st.markdown('<div class="title">🛡️ Phishing Website Detector</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Check whether a website is legitimate or phishing</div>',
    unsafe_allow_html=True
)

# Input
url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

# Button
if st.button("🔍 Analyze Website", use_container_width=True):

    if not url:
        st.warning("Please enter a URL.")
    else:

        features = extract_features(url)

        prediction = model.predict([features])

        st.markdown("### Analysis Result")

        if prediction[0] == 1:
            st.markdown(
                '<div class="result-danger">⚠️ Phishing Website Detected</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-safe">✅ Legitimate Website</div>',
                unsafe_allow_html=True
            )

# Footer
st.markdown("""
<div class="footer">
Built with ❤️ using Python, Streamlit and Machine Learning
</div>
""", unsafe_allow_html=True)