import re
import process_data
import markov
import trie
import haiku

corpus = process_data.process(path = "src/data/corpus_syllables.txt") #ladataan ja käsitellään tekstiaineisto
haiku = haiku.Haiku()
k_order = haiku.k_order() #haetaan käyttäjältä markovin ketjun haluttu aste
markov_model = markov.MarkovModel(k_order, corpus)
markov_chain = markov_model.build_model() #luodaan markovin ketju halutun asteen mukaan
trie = trie.Trie()
trie.trie_insert_markov_chain(markov_chain) #tallennetaan sekvenssit ja frekvenssit trieen
content = trie.generate(k_order, length=10)
#content_check = haiku.generate_haiku(content)
for i in content:
    print(i)
    #word = i[0][0]
    #print(word.replace(".", ""))