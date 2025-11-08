import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        print("set up")

    def test_demo(self):
        test = Trie()

        self.assertEqual(str(test), "result is ---") #assertEqual-testi