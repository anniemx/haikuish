import random
from collections import deque
import trie


class Haiku():
    def __init__(self):
        self.poem = []
        self.trie = trie.Trie()

    def k_order(self):
        k_order = int(input("Anna Markovin ketjun aste: "))
        if k_order < 1 or k_order > 10:
            self.k_order()
        return k_order
    
    def create_trie(self, k, corpus):
        n = k + 1
        for sentence in corpus: 
            for i in range(len(sentence) - n + 1):
                self.trie.trie_insert(sentence[i: i + n])

    def lottery(self, words): #words ([words], [frequencies])
        wordlist = words[0]
        weights = words[1]
        next_word = random.choices(wordlist, weights, k=1)
        return next_word[0]

    def generate_haiku(self, k_order):
        search_words = deque(maxlen=k_order)
        
        #generate line 1:
        line_1 = []
        limit = 5
        while limit > 0:
            followers = self.trie.trie_get_followers(search_words, limit)
            next_word = self.lottery(followers)
            if next_word:
                line_1.append(next_word[0])
                search_words.append(next_word)
                limit -= int(next_word[1])

        self.poem.append(line_1)

        #generate line 2:
        line_2 = []
        limit = 7
        while limit > 0:
            followers = self.trie.trie_get_followers(search_words, limit)
            next_word = self.lottery(followers)
            if next_word:
                line_2.append(next_word[0])
                search_words.append(next_word)
                limit -= int(next_word[1])

        self.poem.append(line_2)

        #generate line 3:
        line_3 = []
        limit = 5
        while limit > 0:
            #search valid followers from trie
            followers = self.trie.trie_get_followers(search_words, limit)
            next_word = self.lottery(followers) #call lottery
            if next_word:
                line_3.append(next_word[0])
                search_words.append(next_word)
                limit -= int(next_word[1])

        self.poem.append(line_3)
        self.print_haiku()

    def print_haiku(self):
        #tulosta rivi kerrallaan
        print("***************************")
        print("- Uutishaiku -")
        print("***************************")
        for line in self.poem:
            line = " ".join(line)
            print(line)
        print("***************************")