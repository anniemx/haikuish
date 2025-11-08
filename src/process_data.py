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

#alustetaan tilansiirtomatriisi
def create_transition_matrix(n_words):
    transition_matrix = [[0] * n_words for i in range(n_words)]
    print(len(transition_matrix[1]))
    return transition_matrix

#lasketaan todennäköisyydet sille, että sana esiintyy jonkun sanan jälkeen
def calculate_probabilities(n_grams, n_words, t_matrix):
    prob_words = {}
    for i in n_words:
        for j in ():
            pass

    #for i, word in enumerate(n_words):
    #    for j, next in enumerate(n_words):
    #        count = 0
    #        for n_gram in n_grams:
    #            if n_gram[0] == word and n_gram[1] == next:
    #                count += 1
    #        t_matrix[i][j] = count

    #normalisoidaan matriisi:

    print(t_matrix)
    return t_matrix