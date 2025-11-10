import unittest 
from markov import MarkovModel

#unittest: testauksessa ohjelman yksittäiset funktiot sekä luokkien oliot ja metodit

class TestMarkovModel(unittest.TestCase):
    def setUp(self):
        self.markov = MarkovModel()


    """testataan, että malli rakentuu oikein: n-grammit jakautuu mallin sanakirjarakenteeseen muotoon 
    (sana1, sana2):[(seuraava_sana1, x), (seuraava_sana2, x), (seuraava_sana, x)]"""
    def test_build_model_(self):
        self.assertEqual()

    """testataan, että todennäköisyys oikein"""
    def calculate_prob(self):
        prob =  self.markov
        self.assertEqual()

    """testataan, ettei tyhjiä mjonoja"""
    def test_empty_string(self):
        self.assertEqual("", "")

    """testataan, ettei None"""
    def test_none(self):
        self.assertEqual("", None)

