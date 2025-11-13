import numpy as np
import trie

class Haiku():
    def __init__(self):
        pass

    def starting_word(self):
        self.degree = input("Anna Markovin ketjun aste: ")
        #validoidaan input 1.tavutettu, 2. alle 5 tavua, 3. ei tyhjä

    def generate_haiku(self):
        #tavut kolmella rivillä 5 - 7 - 5 -> miten saadaan varmistettua oikea tavumäärä?
        haiku = [[], [], []]
        i = 1
        #haku 5 tavulle, haku 7-tavulle, haku 5-tavulle vai yksi haku 17 tavulle?
        trie.trie_search(self.start)
        #haku 7 tavulle
        #haku 5 tavulle
        return haiku

    def print_haiku(self, haiku_poem):
        #tulosta rivi kerrallaan
        for line in haiku_poem:
            print(line)