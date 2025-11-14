#import numpy as np
import random as rm
#import process_data

class MarkovModel:
    def __init__(self, k_order, corpus):
        self.k_order = int(k_order)
        self.n_grams = []
        self.words = []
        self.markov_model = {}
        self.corpus = corpus

    #jaetaan tekstiaineisto k+1=n ketjuihin (n-grammeihin)
    def generate_ngrams(self):
        n = self.k_order + 1
        words = self.corpus.split()
        for i in range(len(words) - n + 1):
            self.n_grams.append(words[i : i + n])
        print(self.n_grams)
        return self.n_grams

    def find_unique_words(self):
        word_list = list(set(self.corpus.split()))
        #print(word_list, len(word_list))
        return word_list

    def build_model(self):
        """Muodostetaan mallin sanakirja self.markov_model, jossa n-grammit tuple-avaimena ja lasketaan n-grammien esiintyvyys. 
            Siis tällöin saadaan kahden sanan ja niitä seuraavan sanan esiintyvyysmäärä (frekvenssi) koko tekstissä. 
            -> Tämän jälkeen lasketaan lukumäärän perusteella todennäköisyys sille, että kahta sanaa seuraa tietty sana."""
        
        self.generate_ngrams()

        self.n_grams = [tuple(n_gram) for n_gram in self.n_grams]
        for n_gram in self.n_grams:
            if n_gram in self.markov_model:
                self.markov_model[n_gram] += 1
            else:
                self.markov_model[n_gram] = 1
        values = list(self.markov_model.values())
        #print(self.markov_model, values)

    def calculate_prob(self):
        """lasketaan todennäköisyydet, että kahta sanaa seuraa kolmas sana. 
        Siis sana1, sana2 -> sana3 tarvitaan kahden sanan jälkeiset kaikki 
        mahdolliset sanat, joista lasketaan esiintyvyys riippuen kahdesta edellisestä sanasta."""

        probabilities = {} #tallennetaan sanat ja seuraavien sanojen todennäköisyydet sanakirjaan

        #käydään läpi sanat: onko sana1 ja sana2 löydetty peräkkäin? -> jos ei lisätään sanakirjaan ja arvoksi sana3
        for word in self.markov_model.keys():
            if (word[0], word[1]) not in probabilities:
                probabilities[(word[0], word[1])] = [word[2]]

            else:
                probabilities[(word[0], word[1])].append(word[2])

        for pair in probabilities.keys():
            """avaimena kaksi edellistä tilaa -> (sana1, sana2): [(sana3, tod.näk), (sana4, tod.näk)] <- mahdolliset 
            seuraavat sanat ja niiden todennäköisyydet suhteessa muihin mahdollisiin seuraaviin sanoihin tuplena listassa"""

            next_words = probabilities[pair]
            words_prob = []
            for word in next_words:
                count = next_words.count(word)
                prob = count / len(next_words)
                words_prob.append((word, prob))

            probabilities[pair] = words_prob
            
        #print(probabilities)
        return probabilities

        #print(probabilities, len(probabilities))