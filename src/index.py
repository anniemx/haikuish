import process_data
import markov
import trie
import haiku

def main():
    #ladataan ja käsitellään tekstiaineisto
    corpus = process_data.process(path = "src/data/corpus_syllables.txt")
    haiku_poem = haiku.Haiku()
    k_order = haiku_poem.k_order() #haetaan käyttäjältä markovin ketjun haluttu aste
    #luodaan markovin ketju halutun asteen mukaan
    markov_model = markov.MarkovModel(k_order, corpus)
    markov_chain = markov_model.build_model()
    trie_tree = trie.Trie()
    trie_tree.trie_insert_markov_chain(markov_chain) #tallennetaan sekvenssit ja frekvenssit trieen

    #generoidaan sanat ja tarkastetaan haikumuoto
    try:
        content = trie_tree.generate(k_order, length=500)
        haiku_poem.print_haiku(content)
    except:
        print("Haikumuotoa noudattavia runoja ei löytynyt.")

if __name__=="__main__":
    main()