import process_data
import markov
import trie
import haiku

corpus = process_data.pre_process() #ladataan ja käsitellään tekstiaineisto
haiku = haiku.Haiku() 
k_order = haiku.k_order() #haetaan käyttäjältä markovin ketjun haluttu aste
markov_model = markov.MarkovModel(k_order, corpus) 
markov_model = markov_model.build_model() #luodaan markovin ketju halutun asteen mukaan
trie = trie.Trie()
trie.trie_insert_markov_chain(markov_model) #tallennetaan sekvenssit ja frekvenssit trieen
