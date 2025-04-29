import requests
import json
import numpy as np


def emotion_detector(text_to_analyse: str) -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyse } }
    res = json.loads(
        requests.post(
            url, 
            headers=headers,
            json=json_input
        ).text
    )
    
    formatted_response: dict[str, float] = {}

    highest_score: int = 0

    for emotion, score in res['emotionPredictions'][0]['emotion'].items():
        formatted_response[emotion] = score
        if score > highest_score:
            dominant_emotion = emotion
            highest_score = score

    formatted_response['dominant_emotion'] = dominant_emotion

    return formatted_response