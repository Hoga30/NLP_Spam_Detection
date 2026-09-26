import streamlit as st
import joblib


# Load the trained model and TF-IDF vectorizer
model = joblib.load("models/spam_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")


# Page configuration
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📱"
)


# App title
st.title("📱 SMS Spam Detector")

st.write(
    "Enter an SMS message below and the NLP model will predict "
    "whether it is Ham or Spam."
)


# Text input
message = st.text_area(
    "Enter your SMS message:",
    placeholder="Example: Congratulations! You have won a prize!"
)


# Prediction button
if st.button("Check Message"):

    if message.strip() == "":
        st.warning("Please enter an SMS message.")

    else:
        # Convert message into TF-IDF features
        message_tfidf = tfidf.transform([message])

        # Make prediction
        prediction = model.predict(message_tfidf)[0]

        # Get prediction probabilities
        probabilities = model.predict_proba(message_tfidf)[0]

        confidence = probabilities[prediction] * 100

        # Display result
        if prediction == 1:
            st.error("🚨 SPAM")
        else:
            st.success("✅ HAM — Not Spam")

        st.write(f"Confidence: **{confidence:.2f}%**")