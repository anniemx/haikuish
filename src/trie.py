import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEndof = False
        self.frequency = 0


class Trie: 
    def __init__(self):
        self.root = TrieNode()

    def trie_insert(self, corpus): #time complexity O(n), space complexity O(n)
        current_node = self.root
        for word in corpus:
            current_node.frequency += 1
            if word not in current_node.children:
                current_node.children[word] = TrieNode()
            current_node = current_node.children[word]
        current_node.frequency += 1
        current_node.IsEndof = True

    #check the path of wordlist exists, return the last word
    def get_node(self, wordlist):
        node = self.root
        for word in wordlist:
            if word not in node.children:
                return None
        return node

    #search the followers of last word from wordlist, return all valid words (limit)
    def trie_search_followers(self, search_words, limit): #time complexity O(n), space complexity O(1)
        node = self.get_node(search_words)
        following_words = []
        if not node:
            return following_words
        for word, child in node.children.items():
            if limit <= word[1]:
                following_words.append(word[0], child.frequency)
        return following_words

