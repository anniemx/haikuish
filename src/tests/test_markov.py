import unittest
from markov import MarkovModel

class TestMarkovModel(unittest.TestCase):
    def setUp(self):
        print("set up")

    def test_demo(self):
        test = MarkovModel()

        self.assertEqual(str(test), "result is ---")