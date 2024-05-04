''' Implement on localhost:5000
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text and runs emotion_detector
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    keys = list(response.keys())
    values = list(response.values())
    if values[0] is None:
        return "Invalid text! Please try again!"
    return "For the given statement, the system response is {}: {}, {}: {}, {}: {}, {}: {} and {}: {}. The dominant emotion is {}.".format(
            keys[0], values[0], keys[1], values[1], keys[2], values[2], keys[3], values[3], keys[4], values[4], values[5])


@app.route("/")
def render_index_page():
    ''' This function renders the main
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This function deploys on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
