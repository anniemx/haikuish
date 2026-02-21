#from src import process_data
#from src.haiku import Haiku

"""End-to-end testing
    1. set up: two generated haiku poems
    2. generate ngrams from the haiku k-order
    3. check if the ngrams exist in the original corpus
    """
class MarkovTest():

    def process_data(self, path):
        data = open(path, encoding="utf-8").read()
        data = data.split("\n")
        corpus = []

        for line in data:
            all_words = line.split(" ")
            sentence = []
            for word in all_words:
                word_syllables = word.split(":")
                word = (word_syllables[0], int(word_syllables[1]))
                sentence.append(word)
            corpus.append(sentence)

        return corpus

    def test_markov_chain(self, poem):
        #generate n-grams from haiku
        n = 3 #k-order 2+1
        haiku_words = poem.split()
        haiku_ngrams = []
        for i in range(len(haiku_words) - n + 1):
            haiku_ngrams.append(haiku_words[i: i + n])
        
        corpus_ngrams = []
        self.corpus = self.process_data(path = "src/data/test_corpus.txt")
        for sentence in self.corpus:
            for i in range(len(sentence) - n + 1):
                ngram1 = sentence[i: i + n]
                ngram_words = []
                for word in ngram1: 
                    ngram_words.append(word[0]) #[sana1, sana2, sana3]
                corpus_ngrams.append(ngram_words)

        result = []
        #search haiku-ngrams from data-ngrams
        for ngram in haiku_ngrams:
            if ngram in corpus_ngrams:
                result.append(ngram)

        assert result == haiku_ngrams

if __name__=="__main__":
    test_markov = MarkovTest()
    poem1 = "riikolan mukaan englannin kieli on jo odottamassa"
    poem2 = "pasi tinnilän liberi oy ja vr group lähtökohtana"
    try: 
        test_markov.test_markov_chain(poem1)
        test_markov.test_markov_chain(poem2)
        print("Tests passed")
    except:
        print("not passed")
