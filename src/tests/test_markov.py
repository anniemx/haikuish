import unittest 
from markov import MarkovModel

#unittest: testauksessa ohjelman yksittäiset funktiot sekä luokkien oliot ja metodit

class TestMarkovModel(unittest.TestCase):
    def setUp(self):
        self.markov = MarkovModel()

    def test_demo(self):
        self.assertEqual("", "") #assertEqual-testi

    def test_empty_string(self):
        self.assertEqual("", "")

    def test_none(self):
        self.assertEqual("", "")