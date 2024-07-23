"""
Emotion Detector Flask Application

This module sets up a Flask web application for detecting emotions in text.
It includes routes for rendering the index page and analyzing emotions in the provided text.

Routes:
- /: Render the index page.
- /emotionDetector: Analyze emotions in the provided text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        HTML template for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyser():
    """
    Analyze the emotions in the provided text.

    Retrieves the text to analyze from the query parameters, uses the emotion_detector function to
    analyze the text, and returns a formatted response indicating the detected emotions.

    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions.

    Returns:
        str: A string summarizing the detected emotions and the dominant emotion.
             Returns an error message if the text is invalid.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    formatted = emotion_detector(text_to_analyse)

    anger = formatted['anger']
    disgust = formatted['disgust']
    fear = formatted['fear']
    joy = formatted['joy']
    sadness = formatted['sadness']
    dominant = formatted['dominant_emotion']

    if anger is None:
        return "Invalid text! Try again."
    return (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
            f"The dominant emotion is {dominant}"
        )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
