import re
#import numpy as np
#import nltk
#from nltk import ngrams

corpus = ("""Lorem ipsum dolor sit amet, 
          consectetur adipiscing elit. Nullam 
          nec lobortis nulla. Curabitur congue 
          interdum eros commodo suscipit. Phasellus 
          feugiat aliquam molestie. Nam est urna, pharetra 
          viverra auctor et, pellentesque quis ligula. 
          Morbi in consectetur ligula. Mauris eros est, 
          egestas ut vehicula vitae, volutpat at mi. Aliquam 
          posuere volutpat turpis.""")   #open("").read()

corpus = re.sub(r"[^a-zA-Z0-9\s]", "", corpus)
corpus = corpus.lower()

def process():
    all_n_grams = generate_ngrams(corpus)
    all_words = find_unique_words(corpus)
    trasition_matrix = create_transition_matrix(len(all_words))


#jaetaan tekstiaineisto kolmen sanan ketjuihin (n-grammeihin, n=3)
def generate_ngrams(corpus):
    n = 3
    words = corpus.split()
    n_grams = []
    for i in range(len(words) - n + 1):
        n_grams.append(words[i : i + n])
    print(n_grams)
    return n_grams

    #n_grams = ngrams(text.split(), n)
    #n_grams = list(n_grams)

def find_unique_words(corpus):
    word_list = list(set(corpus.split()))
    print(word_list, len(word_list))
    return word_list

def create_transition_matrix(n_words):
    transition_matrix = [[0] * n_words for i in range(n_words)]
    print(len(transition_matrix[1]))
    return transition_matrix

def calculate_probabilities():
    pass