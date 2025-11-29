import unittest
from trie import Trie


#trien tarkastuksessa tärkein: toimiiko tallennus ja haku oikein: rakenne
#mitä palautetaan tyhjillä tai none-syötteillä?


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.content = {("sana1", "sana2", "sana3"): 2,
                        ("sana2", "sana3", "sana4"): 1,
                        ("sana3", "sana4", "sana5"): 1,
                        }
        self.trie.trie_insert_markov_chain(self.content)

    def trie_insert_markov_chain(self):
        self.assertTrue(self.trie.trie_search(("sana1", "sana2", "sana3")))
        self.assertTrue(self.trie.trie_search(("sana2", "sana3", "sana4")))
        self.assertTrue(self.trie.trie_search(("sana3", "sana4", "sana5")))

    def generate(self):
        self.assertTrue("", "")

    def test_search_empty_string(self):
        self.assertEqual(self.trie.trie_search(""), False)

    def test_search_none(self):
        self.assertEqual(self.trie.trie_search(None), False)

    def test_search(self):
        self.assertTrue(self.trie.trie_search(("sana3", "sana4", "sana5")))

if __name__=="__main__":
    unittest.main()
