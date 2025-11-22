import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.content = {("sana1", "sana2", "sana3"):2, 
                        ("sana2", "sana3", "sana4"):1, 
                        ("sana3", "sana4", "sana5"):1,
                        }
        self.trie_insert_markov_chain(self.content)

    def trie_insert_markov_chain(self):
        self.assertTrue(self.trie.trie_search(("sana1", "sana2", "sana3")))
        self.assertTrue(self.trie.trie_search(("sana2", "sana3", "sana4")))
        self.assertTrue(self.trie.trie_search(("sana3", "sana4", "sana5")))

    def generate(self):
        self.assertTrue("", "")
    

    #tyhjä markov ketju?
    def test_insert_empty_string(self):
        self.assertEqual("", "")

    def test_insert_none(self):
        self.assertEqual("", "")

