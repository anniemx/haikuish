from src import process_data
from src import haiku

"""End-to-end testing
    1. load testing data, generate ngrams k-order
    2. generate haiku
    3. generate ngrams from the haiku k-order
    4. check if the ngrams exist in the original corpus
    """

def test_markov_chain():
    #load and process corpus
    corpus = process_data.process(path = "src/data/test_corpus.txt")
    haiku_poem = haiku.Haiku()
    k_order = 2
    #insert sentences by k+1 ngrams to trie
    haiku_poem.create_trie(k_order, corpus)

    try:
        haiku_poem.generate_haiku(k_order)
    except:
        print("Haikumuotoa noudattavia runoja ei voitu generoida.")
    
    #generate n-grams from haiku
    haiku_words = [word for line in haiku_poem for word in line]
    corpus_ngrams = []
    n_grams = []
    n = k_order + 1

    for sentence in corpus: 
        for i in range(len(sentence) - n + 1):
            ngram1 = sentence[i: i + n]
            ngram_words = []
            for word in ngram1: #[sana1:1 sana2:2 sana3:2]
                ngram_words.append(word[0])
            corpus_ngrams.append(ngram_words)

    for i in range(len(haiku_words) - n + 1):
        n_grams.append(haiku_words[i: i + n])

    result = []
    #search haiku-ngrams from data-ngrams
    for ngram in n_grams:
        if ngram in corpus_ngrams:
            result.append(ngram)

    assert result == n_grams

if __name__=="__main__":
    test_markov_chain()
