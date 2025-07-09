"""Flask web app for Emotion Detection.

Provides two endpoints:

  * GET /            → renders the HTML form
  * GET /emotionDetector?textToAnalyze=… 
                     → returns the emotion scores and dominant emotion
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route('/emotionDetector')
def emo_detector():
    """Analyze a piece of text and return emotion scores plus dominant emotion.

    Reads the `textToAnalyze` query parameter, passes it to `emotion_detector()`,
    and returns a formatted string containing anger, disgust, fear, joy, sadness,
    and which one is dominant.

    Returns:
        str: HTML snippet summarizing the scores or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
        )


@app.route('/')
def render_index_page():
    """Render the main index page with the emotion-input form."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
