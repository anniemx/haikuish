import re
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

def process():
    generate_ngrams(corpus)

#jaetaan tekstiaineisto 3 sanan ketjuihin (n-grammeihin, n=3)
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

