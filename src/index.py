import process_data
import haiku

def main():
    #load and process corpus
    corpus = process_data.process(path = "src/data/test_corpus.txt")
    #start haiku poem by asking k-order
    haiku_poem = haiku.Haiku()
    k_order = haiku_poem.k_order()
    #insert sentences by k+1 ngrams to trie
    haiku_poem.create_trie(k_order, corpus)
    #try generating haiku line by line
    try:
        haiku_poem.generate_haiku(k_order)
    except:
        print("Haikumuotoa noudattavia runoja ei voitu generoida.")

if __name__=="__main__":
    main()