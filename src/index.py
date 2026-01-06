import process_data
import haiku

def main():
    #load and process corpus
    corpus = process_data.process(path = "src/data/corpus_syllables.txt")
    #start haiku poem by asking k-order
    haiku_poem = haiku.Haiku()
    k_order = haiku_poem.k_order()
    haiku_poem.create_trie(k_order, corpus)
    """try:
        pass
    except:
        print("Haikumuotoa noudattavia runoja ei löytynyt.")"""

if __name__=="__main__":
    main()