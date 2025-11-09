import unittest
from trie import Trie

#unittest: testauksessa ohjelman yksittäiset funktiot sekä luokkien oliot ja metodit

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie
        self.trie_insert_markov_chain("")
        self.trie_insert("")
        self.trie_insert("")
        self.trie_insert("")

    def test_demo(self):
        self.assertEqual("", "") #assertEqual-testi
    
    def test_insert_empty_string(self):
        self.assertEqual("", "")

    def test_insert_none(self):
        self.assertEqual("", "")