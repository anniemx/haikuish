import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.content = {("testaus", "teksti", "jossa"): 1, ("teksti", "jossa", "on"): 1,
                        ("jossa", "on", "useampi"): 1, ("on", "useampi", "lapsi") : 1,
                        ("useampi", "lapsi", "ja"): 1, ("lapsi", "ja", "useampi"): 1,
                        ("ja", "useampi", "sana"): 3, ("useampi", "sana", "jotta"): 1,
                        ("sana", "jotta", "nähdään"): 1, ("jotta", "nähdään", "jakaako"): 1,
                        ("nähdään", "jakaako", "trie"): 1, ("jakaako", "trie", "tietorakenteeseen"): 1,
                        ("trie", "tietorakenteeseen", "oikein"): 1}
        self.trie.trie_insert_markov_chain(self.content)

    def test_trie_insert_markov_chain(self):
        self.assertTrue(self.trie.trie_search(("ja", "useampi", "sana")))
        self.assertTrue(self.trie.trie_search(("useampi", "sana", "jotta")))
        self.assertTrue(self.trie.trie_search(("trie", "tietorakenteeseen", "oikein")))

    def test_search_empty_string(self):
        self.assertEqual(self.trie.trie_search(""), False)

    def test_search_none(self):
        result = self.trie.generate(None, None)
        self.assertEqual(result, [])

    def test_structure(self):
        print(self.trie)
