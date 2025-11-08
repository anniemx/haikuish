import re
#import numpy as np
#import nltk
#from nltk import ngrams


corpus = ("""Lorem ipsum dolor sit amet, feugiat aliquam molestie, feugiat aliquam molestie
          consectetur adipiscing elit. Nullam Curabitur congue
          nec lobortis nulla. Curabitur congue Curabitur congue Curabitur congue Curabitur congue
          interdum eros commodo suscipit. Phasellus Curabitur congue
          feugiat aliquam molestie. Nam est urna, pharetra 
          viverra auctor et, eros commodo suscipit pellentesque quis ligula.
          Morbi in consectetur ligula. Mauris eros est, 
          egestas ut eros commodo suscipit  vehicula vitae, volutpat at mi. Aliquam 
          posuere volutpat turpis auctor et, eros commodo suscipit pellentesque quis ligula.
          Morbi in consectetur ligula. Mauris eros est,
          egestas ut eros commodo suscipit  vehicula vitae, volutpat at mi. Aliquam
          posuere volutpat turpis.""")   #open("").read()

corpus = re.sub(r"[^a-zA-Z0-9\s]", "", corpus)
corpus = corpus.lower()

def process():
    all_n_grams = generate_ngrams(corpus)
    unique_words = find_unique_words(corpus)
    #trasition_matrix = create_transition_matrix(len(unique_words))
    #calculate_probabilities(all_n_grams, unique_words, trasition_matrix)
    return all_n_grams, unique_words

#jaetaan tekstiaineisto kolmen sanan ketjuihin (n-grammeihin, n=3)
def generate_ngrams(corpus):
    n = 3
    words = corpus.split()
    n_grams = []
    for i in range(len(words) - n + 1):
        n_grams.append(words[i : i + n])

    #print(n_grams)
    return n_grams

def find_unique_words(corpus):
    word_list = list(set(corpus.split()))
    #print(word_list, len(word_list))
    return word_list

