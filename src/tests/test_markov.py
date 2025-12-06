import markov
import trie
import process_data
import haiku

""" Päästä-päähän testaus
    1. lataa testitekstiaineisto (pienempi ja kevyempi), muodosta sen n-grammit
    2. generoi haiku
    3. muodosta runosta n-grammit
    4. etsi löytyykö muodostetut n-grammit alkuperäisestä aineistosta
    """

class TestMarkovModel():
    def setUp(self):
        self.corpus = process_data.process(path="src/data/test_corpus.txt")
        self.haiku = haiku.Haiku()
        self.markov_model = markov.MarkovModel(k_order = 2, corpus = self.corpus)
        self.markov_chain = self.markov_model.build_model()
        self.trie = trie.Trie()
        self.trie.trie_insert_markov_chain(self.markov_chain)
        self.content = self.trie.generate(k_order = 2, length = 5)

    def test_demo(self):
        self.haiku_markov_model = markov.MarkovModel(k_order = 2, corpus = self.content)
        haiku_markov_chain = self.markov_model.build_model()

        for item in haiku_markov_chain:
            if item not in self.markov_chain:
                return False
        return True
    
    def test_print(self, result):
        if result is True:
            print("Markov chain test: passed")
        else:
            print("Markov chain test: failed")


if __name__=="__main__":
    test_markov = TestMarkovModel()
    test_result = test_markov.test_demo()
    test_markov.test_print(test_result)
