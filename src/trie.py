class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    #etsitään trie-puusta sana kirjain kerrallaan child = kirjain
    def trie_search(self, word):
        current_node = self.root

        for child in word: # käydään läpi kirjaimet sanasta
            if child not in current_node.children:
                #palautetaan epätosi -> sana ei puussa, kirjainta ei löydy oikeassa järjestyksessä
                return False 
            
            current_node = current_node.children[child]

        return current_node.is_end_of_word #palautetaan tieto, että saavutettiin sanan loppu

    def c(self, markov_chain):
        for n_gram in markov_chain:

           Trie.trie_insert(n_gram)

    #lisätään n-grammit trie-puuhun tavutettuna merkkijonona
    def trie_insert(self, n_gram):
        current_node = self.root
        #lisätään sana tavu kerrallaan -> luodaan uusi solmu, jos tavu ei puussa
        for child in n_gram:
            if child not in current_node.children:
                current_node.children[child] = TrieNode()

            current_node = current_node.children[child]
        #kirjainten lopuksi merkitään sana päättyneeksi is_end_of_word=True
        current_node.is_end_of_word = True

    def trie_delete(self, word):
        self.help_delete(self.root, word, 0)

    def help_delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word():
                return False
            
            current_node.is_end_of_word = False #poistetaan vain tieto sanan lopusta
            return len(current_node.children) == 0
        
        child = word[index]
        node = current_node.children.get(child)

        if node is None:
            return False
        
        #poistetaan rekursiivisesti, jos puulla ei lehtiä poiston jälkeen
        delete_current_node = self.help_delete(node, word, index + 1) 
        if delete_current_node:
            del current_node.children[child]
            return len(current_node.children) == 0 and not current_node.is_end_of_word

    def has_prefix(self, prefix): #löytyykö sanan etuliite?
        current_node = self.root

        for child in prefix: # käydään läpi kirjaimet sanasta
            if child not in current_node.children:
                #palautetaan epätosi -> etuliite ei puussa, kirjainta ei löydy oikeassa järjestyksessä
                return False 
            
            current_node = current_node.children[child]

        return True #palautetaan tieto, että saavutettiin sanan loppu


    def starts_with(self, prefix): #käytetään DFS
        words = [] #kerätään löydetyt sanat listaan
        current_node = self.root

        for child in prefix:
            if child not in current_node.children:
                return words

            current_node = current_node.children[child]

        def dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append("".join(path)) #koostetaan sana mjonoksi

            for child, child_node in current_node.children.items():
                dfs(child_node, path + [child])

            dfs(current_node, list(prefix))

            return words

    def list_words(self):
        words = []

        def dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append("".join(path)) #koostetaan sana mjonoksi

            for child, child_node in current_node.children.items():
                dfs(child_node, path + [child])

            dfs(self.root, [])

            return words

