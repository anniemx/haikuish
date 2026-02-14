
class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        trie_content = []

        def _dfs(node, visited):
            visited.add(node)
            for key, child in node.children.items():
                trie_content.append(key[0]+str(child.frequency)+"-")
                if child not in visited:
                    _dfs(child, visited)

        _dfs(self.root, set())
        return "".join(trie_content)

    def trie_insert(self, ngram):
        """Function inserting ngrams to trie"""

        current_node = self.root
        for word in ngram:
            if word not in current_node.children:
                current_node.children[word] = TrieNode()
            current_node = current_node.children[word]
            current_node.frequency += 1

    def trie_search(self, ngram):
        """Function searching words/ngrams from trie, return False/True."""

        if not ngram:
            return False
        node = self.root
        for word in ngram:
            if word not in node.children:
                return False
            node = node.children[word]
        return True


    def get_node(self, wordlist):
        """Function to check whether the path of wordlist exists, 
            return None/the last word."""

        node = self.root
        for word in wordlist:
            if word not in node.children:
                return None
            node = node.children[word]
        return node


    def trie_get_successors(self, search_words, limit):
        """Getter to search the successors of last word from wordlist, 
            return all valid words considering syllable limit."""

        node = self.get_node(search_words)
        successors_words = []
        successors_frequencies = []
        if not node:
            return (successors_words, successors_frequencies)
        for child, child_node in node.children.items():
            if child[1] <= limit:
                successors_words.append(child)
                successors_frequencies.append(child_node.frequency)
        return (successors_words, successors_frequencies)
