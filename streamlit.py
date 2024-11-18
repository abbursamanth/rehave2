import streamlit as st
from textblob import TextBlob

# Hardcoded songs for meditation based on mood (using YouTube links for song playing)
song_suggestions = {
    "Happy": [
        ("Happy by Pharrell Williams", "https://www.youtube.com/watch?v=YbN6WmXwoA8"),
        ("Can't Stop the Feeling! by Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
        ("Uptown Funk by Mark Ronson ft. Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0")
    ],
    "Sad": [
        ("Weightless by Marconi Union", "https://www.youtube.com/watch?v=5di6EYVi7G8"),
        ("Sunset Lover by Petit Biscuit", "https://www.youtube.com/watch?v=3dbSgEr1tZ4"),
        ("Don't Let the Sun Go Down on Me by Elton John", "https://www.youtube.com/watch?v=2sTgtK_hgrY")
    ],
    "Neutral": [
        ("Breezeblocks by Alt-J", "https://www.youtube.com/watch?v=VZRqzR6Wngs"),
        ("Sitting, Waiting, Wishing by Jack Johnson", "https://www.youtube.com/watch?v=8QkQyF7u6Wo"),
        ("Dreams by Fleetwood Mac", "https://www.youtube.com/watch?v=mrZRURcb1cM")
    ]
}

# Function to analyze sentiment and predict mood
def analyze_sentiment(user_input):
    combined_input = ' '.join(user_input.values())
    blob = TextBlob(combined_input)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Happy"
    elif sentiment < 0:
        return "Sad"
    else:
        return "Neutral"

# Streamlit UI
st.title("Mood Prediction and Meditation Song Suggestions")

# Create a form with 3 questions
with st.form("mood_form"):
    answer1 = st.text_area("How are you feeling today?")
    answer2 = st.text_area("What did you do today?")
    answer3 = st.text_area("What are you expecting from today?")

    # Submit button
    submit_button = st.form_submit_button("Submit")

if submit_button:
    # Collect answers into a dictionary
    user_answers = {
        "answer1": answer1,
        "answer2": answer2,
        "answer3": answer3
    }

    # Get mood prediction
    mood = analyze_sentiment(user_answers)

    # Save mood in Streamlit session state
    st.session_state.mood = mood

    # Display the predicted mood
    st.write(f"Your mood is predicted as: {mood}")

    # Suggest meditation songs based on mood
    if mood in song_suggestions:
        st.write("We suggest the following songs for meditation:")
        for song, url in song_suggestions[mood]:
            st.write(f"- {song}")
            # Embed the YouTube player for each song
            st.video(url)
