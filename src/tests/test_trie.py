import unittest
from ..trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.content = {(("testaus", 2), ("teksti", 2), ("jossa", 2)): 1, 
                        (("teksti", 2), ("jossa", 2), ("on", 2)): 1,
                        (("jossa", 2), ("on", 2), ("useampi", 3)): 1, 
                        (("on", 2), ("useampi", 3), ("lapsi", 2)) : 1,
                        (("useampi", 3), ("lapsi", 2), ("ja", 1)): 1, 
                        (("lapsi", 2), ("ja", 1), ("useampi", 4)): 1,
                        (("ja", 1), ("useampi", 4), ("sana", 2)): 3, 
                        (("useampi", 4), ("sana", 2), ("jotta", 2)): 1,
                        (("sana", 2), ("jotta", 2), ("nähdään", 2)): 1, 
                        (("jotta", 2), ("nähdään", 2), ("jakaako", 3)): 1,
                        (("nähdään", 2), ("jakaako", 3), ("trie", 1)): 1, 
                        (("jakaako", 3), ("trie", 1), ("rakenteeseen", 4)): 1,
                        (("trie", 1), ("rakenteeseen", 4), ("oikein", 2)): 1}
        self.trie.trie_insert_markov_chain(self.content)

    def test_trie_insert_markov_chain(self):
        self.assertTrue(self.trie.trie_search((("ja", 1), ("useampi", 4), ("sana", 2))))
        self.assertTrue(self.trie.trie_search((("jotta", 2), ("nähdään", 2), ("jakaako", 3))))
        self.assertTrue(self.trie.trie_search((("trie", 1), ("rakenteeseen", 4), ("oikein", 2))))

    def test_search_empty_string(self):
        self.assertEqual(self.trie.trie_search(""), False)

    def test_search_none(self):
        result = self.trie.generate(None, None)
        self.assertEqual(result, [])

    def test_structure(self):
        print(self.trie)
