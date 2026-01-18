import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.trie_insert([('on', '1'), ('virrannut', '3'), ('lastenlaulukulttuurin', '7')])
        self.trie.trie_insert([('virrannut', '3'), ('lastenlaulukulttuurin', '7'), ('uudistamisesta', '6')])
        self.trie.trie_insert([('lastenlaulukulttuurin', '7'), ('uudistamisesta', '6'), ('ja', '1')])
        self.trie.trie_insert([('on', '1'), ('olemassa', '4'), ('monia', '3')])
        self.trie.trie_insert([('on', '1'), ('olemassa', '4'), ('ainakin', '3')])

    def test_trie_insert(self):
        self.assertTrue(self.trie.trie_search([('on', '1'), ('virrannut', '3'), ('lastenlaulukulttuurin', '7')]))
        self.assertTrue(self.trie.trie_search([('virrannut', '3'), ('lastenlaulukulttuurin', '7'), ('uudistamisesta', '6')]))
        self.assertTrue(self.trie.trie_search([('lastenlaulukulttuurin', '7'), ('uudistamisesta', '6'), ('ja', '1')]))
        self.assertTrue(self.trie.trie_search([('on', '1'), ('olemassa', '4'), ('monia', '3')]))
        self.assertTrue(self.trie.trie_search([('on', '1'), ('olemassa', '4'), ('ainakin', '3')]))

    def test_search_empty_sequence(self):
        self.assertEqual(self.trie.trie_search(""), False)

    def test_search_none(self):
        result = self.trie.trie_search(None)
        self.assertEqual(result, False)

    def test_get_followers(self):
        #test structure and syllable filter
        search_words = [('on', '1')]
        search_words2 = [('on', '1'), ('olemassa', '4')]
        limit1 = 5
        limit2 = 3
        result1 = self.trie.trie_get_followers(search_words, limit1)
        result2 = self.trie.trie_get_followers(search_words, limit2)
        result3 = self.trie.trie_get_followers(search_words2, limit1)
        self.assertEqual(len(result1[0]), 2) #2 children should be "virrannut" and "olemassa"
        self.assertEqual(len(result2[0]), 1) #1 child should be "virrannut"
        self.assertEqual(len(result3[0]), 2) #2 children should be "monia" and "ainakin"
        

