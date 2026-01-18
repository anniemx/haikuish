
class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0


class Trie: 
    def __init__(self):
        self.root = TrieNode()

    def trie_insert(self, ngram):
        current_node = self.root
        for word in ngram:
            if word not in current_node.children:
                current_node.children[word] = TrieNode()
            current_node = current_node.children[word]
            current_node.frequency += 1

    def trie_search(self, ngram):
        if not ngram:
            return False

        node = self.root

        for word in ngram:
            if word not in node.children:
                return False
            node = node.children[word]

        return True

    #check the path of wordlist exists, return the last word
    def get_node(self, wordlist):
        node = self.root
        for word in wordlist:
            if word not in node.children:
                return None
            node = node.children[word]
        return node


    #search the followers of last word from wordlist, return all valid words (limit)
    def trie_get_followers(self, search_words, limit):
        node = self.get_node(search_words)
        following_words = []
        following_frequencies = []
        if not node:
            return (following_words, following_frequencies)
        for child, child_node in node.children.items():
            if int(child[1]) <= limit:
                following_words.append(child)
                following_frequencies.append(child_node.frequency)
        return (following_words, following_frequencies)