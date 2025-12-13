import process_data
import markov
import trie
import haiku


#ladataan ja käsitellään tekstiaineisto
corpus = process_data.process(path = "src/data/corpus_syllables.txt")
haiku = haiku.Haiku()
k_order = haiku.k_order() #haetaan käyttäjältä markovin ketjun haluttu aste
#luodaan markovin ketju halutun asteen mukaan
markov_model = markov.MarkovModel(k_order, corpus)
markov_chain = markov_model.build_model()
trie = trie.Trie()
trie.trie_insert_markov_chain(markov_chain) #tallennetaan sekvenssit ja frekvenssit trieen

#generoidaan sanat ja tarkastetaan haikumuoto
try:
    content = trie.generate(k_order, length=500)
    haiku.print_haiku(content)
except:
    print("Haikumuotoa noudattavia runoja ei löytynyt.")
