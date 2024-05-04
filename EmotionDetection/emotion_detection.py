import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    if response.status_code == 400:
        formatted_response = json.loads(response.text)
        for key in formatted_response:
            formatted_response[key] = None
        return formatted_response
    else:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        max_score = 0
        max_emotion = ''
        for emotion, score in emotions.items():
            if score > max_score:
                max_score = score
                max_emotion = emotion
        # put max_emotion and max_score as the last output in the json
        emotions['dominant_emotion'] = max_emotion
    return emotions