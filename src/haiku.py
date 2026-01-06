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
    
    def create_trie(self, k, corpus):
        trie_tree = trie.Trie()
        n = k + 1
        for sentence in corpus: 
            for i in range(len(sentence) - n + 1):
                trie_tree.trie_insert(sentence[i: i + n])

    def lottery(self, words): #words ([words], [frequencies])
        word_list = words[0]
        weights = words[1]
        next_word = random.choice(word_list, weights, k=1)
        return next_word

    def generate_haiku(self):
        order = self.k_order()
        search_words = deque(maxlen=order)

        #generate line 1:
        line_1 = []
        limit = 5
        while limit < 0:
            followers = trie.trie_search_followers(self, search_words, limit)
            next_word = self.lottery(self, followers)
            if next_word:
                line_1.append(next_word)[0]
                search_words.append(next_word)
                limit -= next_word[1]

        self.poem.append(line_1)

        #generate line 2:
        line_2 = []
        limit = 7
        while limit < 0:
            followers = trie.trie_search_followers(self, search_words, limit)
            next_word = self.lottery(self, followers)
            if next_word:
                line_2.append(next_word)[0]
                search_words.append(next_word)
                limit -= next_word[1]

        self.poem.append(line_2)

        #generate line 3:
        line_3 = []
        limit = 5
        while limit < 0:
            #search valid followers from trie
            followers = trie.trie_search_followers(self, search_words, limit)
            next_word = self.lottery(self, followers) #call lottery
            if next_word:
                line_3.append(next_word)[0]
                search_words.append(next_word)
                limit -= next_word[1]

        self.poem.append(line_3)

    def print_haiku(self, haiku_poem):
        #tulosta rivi kerrallaan
        for line in haiku_poem:
            print(line)