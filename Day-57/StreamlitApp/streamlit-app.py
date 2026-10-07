import streamlit as st
from utils import SentimentPredictor


MODEL_PATH = "sentiment_classifier.joblib"
LABELS = {0: "negative",1: "positive"}


## Inference System
predictor = SentimentPredictor(MODEL_PATH, LABELS)

## Frontend Streamlit
st.title(
    'Welcome to Movie Review Classification tool',
    text_alignment = "center"
)

user_input = st.text_area(
    "Movie Review",
    height=250,
    placeholder = "Example movie review ... "
)

if st.button("Predict Sentiment !", type="secondary"):
    with st.spinner("Prediction in Progress ...", show_time=True):
        if len(user_input) > 0:
            sentiment = predictor.run(user_input)

            color = "green" if sentiment == "Positive" else "red"

            st.markdown(
                f"""
                <h2 style="color: {color}; text-align: center;">
                    {sentiment.capitalize()}
                </h2>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("Please enter a movie review.")



