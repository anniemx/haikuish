import random
import trie


class Haiku():
    def __init__(self):
        self.poem = []
        self.trie = trie.Trie()

    def k_order(self):
        """Function to ask Markov-chain k-order as input from user."""

        k_order = int(input("Anna Markovin ketjun aste: "))
        if k_order < 1 or k_order > 10:
            print("Aste liian suuri tai pieni.")
            self.k_order()
        return k_order

    def create_trie(self, k, corpus):
        """Create trie datastructure and insert sentences from 
            corpus as n-grams based on k-order."""

        n = k + 1
        for sentence in corpus:
            for i in range(len(sentence) - n + 1):
                self.trie.trie_insert(sentence[i: i + n])

    def lottery(self, words): 
        """Function to draw a word with weights based on frequencies."""

        wordlist = words[0]
        weights = words[1]
        next_word = random.choices(wordlist, weights, k=1)
        return next_word[0]

    def generate_haiku(self, k_order):
        """Function to generate 3 lines of haiku poem line by line."""

        search_words = []

        #generate line 1:
        line_1 = []
        limit = 5
        while limit > 0:
            successors = self.trie.trie_get_successors(search_words, limit)
            next_word = self.lottery(successors)
            if next_word:
                line_1.append(next_word[0])
                search_words.append(next_word)
                if len(search_words) > k_order:
                    search_words.pop(0)
                limit -= int(next_word[1])

        self.poem.append(line_1)
        print(self.poem)

        #generate line 2:
        line_2 = []
        limit = 7
        while limit > 0:
            successors = self.trie.trie_get_successors(search_words, limit)
            next_word = self.lottery(successors)
            if next_word:
                line_2.append(next_word[0])
                search_words.append(next_word)
                if len(search_words) > k_order:
                    search_words.pop(0)
                limit -= int(next_word[1])

        self.poem.append(line_2)
        print(self.poem)

        #generate line 3:
        line_3 = []
        limit = 5
        while limit > 0:
            #search valid followers from trie
            successors = self.trie.trie_get_successors(search_words, limit)
            next_word = self.lottery(successors) #call lottery
            if next_word:
                line_3.append(next_word[0])
                search_words.append(next_word)
                if len(search_words) > k_order:
                    search_words.pop(0)
                limit -= int(next_word[1])

        self.poem.append(line_3)
        print(self.poem)
        self.print_haiku()
        return self.poem

    def print_haiku(self):
        """Function to print the generated haiku poem."""

        print("***************************")
        print("- Uutishaiku -")
        print("***************************")
        for line in self.poem:
            line = " ".join(line)
            print(line)
        print("***************************")
