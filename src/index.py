import process_data
import markov
#import nltk
#import numpy

process_data.process()
markov_model = markov.MarkovModel(process_data.process()[0], process_data.process()[1])
markov_model.build_model()
markov_model.calculate_prob()