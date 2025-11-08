#import numpy as np
import random as rm
#import process_data

class MarkovModel:
    def __init__(self, n_grams, words):
        self.n_grams = n_grams
        self.words = words
        self.markov_model = {}

    def build_model(self):
        """Muodostetaan mallin sanakirja self.markov_model, jossa 3-grammit tuple-avaimena ja lasketaan 3-grammien esiintyvyys. 
            Siis tällöin saadaan kahden sanan ja niitä seuraavan sanan esiintyvyysmäärä koko tekstissä. 
            -> Tämän jälkeen lasketaan lukumäärän perusteella todennäköisyys sille, että kahta sanaa seuraa tietty sana."""

        self.n_grams = [tuple(n_gram) for n_gram in self.n_grams]
        for n_gram in self.n_grams:
            if n_gram in self.markov_model:
                self.markov_model[n_gram] += 1
            else:
                self.markov_model[n_gram] = 1
        values = list(self.markov_model.values())
        print(self.markov_model, values)

    def calculate_prob(self):
        pass