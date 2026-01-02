import random
from collections import deque
import trie


class Haiku():
    def __init__(self):
        self.poem = []

    def k_order(self):
        k_order = int(input("Anna Markovin ketjun aste: "))
        if k_order is None or k_order < 1 or k_order > 50:
            self.k_order()
        return k_order
    
    def check_syllables(self):
        pass

    def lottery(self, words): #words ([words], [frequencies])
        word_list = words[0]
        weights = words[1]
        next_word = random.choice(word_list, weights, k=1)[0]
        return next_word

    def generate_haiku(self):
        order = self.k_order()
        search_words = deque(maxlen=order)

        followers = trie.trie_search_followers(self, search_words, limit)

        #call lottery
        self.lottery(self, followers)



    def print_haiku(self, haiku_poem):
        #tulosta rivi kerrallaan
        for line in haiku_poem:
            line[:] = [word[0].replace(".", "") for word_list in line for word in word_list]
            print(line)

            """        self.sequence = []
        self.search_sequence = []
        self.sequence1 = []
        self.sequence2 = []
        self.sequence3 = []
        #haiku-muodon rajat: rivi1:5 - rivi2:7->12 - rivi3:5->17
        self.line_limits = {1:5, 2:12, 3:17}
        self.line_no = 1
        self.syllable_count = 0
        
        
        
        













        """