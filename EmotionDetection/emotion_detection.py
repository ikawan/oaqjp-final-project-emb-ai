import requests 
import json

def emotion_detector(text_to_analyse):
    #getting the response
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    
    jsonified = json.loads(response.text)
    
    if response.status_code == 200:
        emotions_dict = jsonified['emotionPredictions'][0]['emotion']
        
        #getting the emotions' scores
        anger_score = emotions_dict['anger']
        disgust_score = emotions_dict['disgust']
        fear_score = emotions_dict['fear']
        joy_score = emotions_dict['joy']
        sadness_score = emotions_dict['sadness']
    
        dominant = dominant_emotion(emotions_dict)
    
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant
    }
#functions to find the dominant emotion, takes in a dict and returns key value pair
def dominant_emotion(emotions_dict):
    dominant = None     
    for emotion in emotions_dict:
        if dominant is None:
            dominant = emotion        
        elif emotions_dict[emotion] > emotions_dict[dominant]:
            dominant = emotion
    return dominant