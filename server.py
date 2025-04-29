from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector', strict_slashes=False)
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return {'error': 'Text Invalid! Please try again'}, 422

    try: 
        response = emotion_detection.emotion_detector(text_to_analyze)
    except KeyError as e:
        response = {
            'anger': None,
            'sadnedd': None,
            'joy': None,
            'dominant_emotion': None
        }

        return response, 400

    if response['dominant_emotion'] is None:
        return {'error': 'Text Invalid! Please try again'}, 400
    
    return response, 200


@app.route('/')
def index() -> None:
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)