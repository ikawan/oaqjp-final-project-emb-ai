from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        joy = emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual(joy, 'joy')

        anger = emotion_detector("I am really mad about this")['dominant_emotion']
        self.assertEqual(anger, 'anger')

        disgust = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        self.assertEqual(disgust, 'disgust')

        sad = emotion_detector("I am so sad about this")['dominant_emotion']
        self.assertEqual(sad, 'sadness')

        fear = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(fear, 'fear')



unittest.main()