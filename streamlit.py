import streamlit as st
import requests

# Function to get sentiment analysis from backend (Flask server)
def get_sentiment_analysis(user_input):
    url = "http://127.0.0.1:5000/analyzeSentiment"
    response = requests.post(url, json=user_input)
    if response.status_code == 200:
        return response.json().get('prediction', 'Error')
    else:
        return 'Error in getting prediction'

# Streamlit UI
st.title("Mood Prediction with Sentiment Analysis")

# Create a form with 3 questions
with st.form("mood_form"):
    answer1 = st.text_area("How are you feeling today?")
    answer2 = st.text_area("What did you do today?")
    answer3 = st.text_area("What are you expecting from today?")

    # Submit button
    submit_button = st.form_submit_button("Submit")

if submit_button:
    user_answers = {
        "answer1": answer1,
        "answer2": answer2,
        "answer3": answer3
    }

    mood = get_sentiment_analysis(user_answers)
    st.write(f"Your mood is predicted as: {mood}")
