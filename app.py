import streamlit as st
import pickle
import pandas as pd

from feature_extractor import extract_features

# Load model
model = pickle.load(
    open(
        "phishing_url_model.pkl",
        "rb"
    )
)

st.title("🔒 Phishing Website Detection")

st.write(
    "Enter a URL to determine whether it is phishing or legitimate."
)

url = st.text_input(
    "Website URL"
)

if st.button("Check Website"):

    if url == "":
        st.warning(
            "Please enter a URL."
        )

    elif not url.startswith(("http://", "https://")):
        st.error(
            "Please enter a valid URL starting with http:// or https://"
        )

    else:

        features = extract_features(url)

        prediction = model.predict([features])

        if prediction[0] == 1:
            st.error(
                "⚠️ Phishing Website Detected"
            )
        else:
            st.success(
                "✅ Legitimate Website"
            )

        st.subheader("Extracted Features")

        feature_names = [
            "UsingIP",
            "LongURL",
            "ShortURL",
            "Symbol@",
            "Redirecting//",
            "PrefixSuffix-",
            "SubDomains",
            "HTTPS",
            "HTTPSDomainURL",
            "InfoEmail",
            "AbnormalURL"
        ]

        df_features = pd.DataFrame({
            "Feature": feature_names,
            "Value": features
        })

        st.dataframe(
            df_features,
            hide_index=True
        )