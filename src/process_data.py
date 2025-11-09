import re
#import numpy as np
#import nltk
#from nltk import ngrams

#hataantavutttuainisto
corpus = open("src/data/mini_corpus.txt").read()
corpus = re.sub(r"[^a-zA-Z0-9\säöåÄÖå-]", "", corpus)
corpus = corpus.lower()

def process():
    all_n_grams = generate_ngrams(corpus)
    unique_words = find_unique_words(corpus)
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

