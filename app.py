from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyzeSentiment', methods=['POST'])
def analyze_sentiment():
    user_input = request.get_json()
    combined_input = ' '.join(user_input.values())
    blob = TextBlob(combined_input)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        mood = "Happy"
    elif sentiment < 0:
        mood = "Sad"
    else:
        mood = "Neutral"

    return jsonify({'prediction': mood})

if __name__ == '__main__':
    app.run(debug=True)
