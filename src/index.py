import process_data
import markov
import trie
#import nltk
#import numpy

process_data.process()
markov_model = markov.MarkovModel(process_data.process()[0], process_data.process()[1])
markov_model.build_model()
markov_chain = markov_model.calculate_prob()
trie = trie.Trie()
trie.trie_insert_chain(markov_chain)