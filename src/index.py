import random
import process_data
import markov
import trie
import haiku

corpus = process_data.pre_process() #ladataan ja käsitellään tekstiaineisto
haiku = haiku.Haiku() 
k_order = haiku.k_order() #haetaan käyttäjältä markovin ketjun haluttu aste
markov_model = markov.MarkovModel(k_order, corpus) 
markov_chain = markov_model.build_model() #luodaan markovin ketju halutun asteen mukaan
markov_chain_words = markov_model.find_unique_words() #haetaan listana yksittäiset esiintyvät sanat 
trie = trie.Trie()
trie.trie_insert_markov_chain(markov_chain) #tallennetaan sekvenssit ja frekvenssit trieen
length = 1
while True:
    content = trie.generate(k_order, length)
    length +=1
    if haiku.generate_haiku(content):
        break


