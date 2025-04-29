from emotion_detection import emotion_detector

import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self) -> None:
        test_joy = emotion_detector('I am glad this happened')
        self.assertEqual(test_joy['dominant_emotion'],'joy')

        test_anger = emotion_detector('I am really mad about this')
        self.assertEqual(test_anger['dominant_emotion'], 'anger')

        test_disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_disgust['dominant_emotion'], 'disgust')

        test_sadness = emotion_detector('I am so sad about this')
        self.assertEqual(test_sadness['dominant_emotion'], 'sadness')

        test_fear = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_fear['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()