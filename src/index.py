import process_data
import markov
import trie
import haiku
#import numpy

corpus = process_data.pre_process()
haiku = haiku.Haiku()
k_order = haiku.k_order()
markov_model = markov.MarkovModel(k_order, corpus)
markov_model.build_model()
markov_chain = markov_model.calculate_prob()
trie = trie.Trie()
trie.trie_insert_chain(markov_chain)