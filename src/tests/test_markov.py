import unittest 
from markov import MarkovModel

#unittest: testauksessa ohjelman yksittäiset funktiot sekä luokkien oliot ja metodit

class TestMarkovModel(unittest.TestCase):
    def setUp(self):
        self.markov = MarkovModel()

    #testataan muodostuuko n-grammit asteen mukaisesti oikein
    def test_generate_ngrams():
        pass

    """testataan, että malli rakentuu oikein: n-grammit jakautuu mallin sanakirjarakenteeseen muotoon 
    """
    def test_build_model_(self):
        self.assertEqual() #palauttaako sekvenssit ja frekvenssit oikeassa muodossa

    #testataan, ettei tyhjiä mjonoja
    def test_empty_string(self):
        self.assertEqual("", "")

    #testataan, ettei None
    def test_none(self):
        self.assertEqual("", None)

