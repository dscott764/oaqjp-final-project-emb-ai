from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        dominant_emotion = emotion_detector('I am glad this happened')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'joy')

        dominant_emotion = emotion_detector('I am really mad about this')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'anger')

        dominant_emotion = emotion_detector('I feel disgusted just hearing about this')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'disgust')

        dominant_emotion = emotion_detector('I am so sad about this')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'sadness')

        dominant_emotion = emotion_detector('I am really afraid that this will happen')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'fear')

unittest.main()
