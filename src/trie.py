import random

class TrieNode:
    def __init__(self):
        self.children = {} # a: TrieNode
        self.is_end_of_sequence = False
        self.frequency = 1


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

    def trie_insert_markov_chain(self, markov_chain):
        for n_gram in markov_chain:

           Trie.trie_insert(n_gram)

    #lisätään n-grammit trie-puuhun sanoittain
    def trie_insert(self, n_gram):
        current_node = self.root
        #lisätään sana kerrallaan -> luodaan uusi solmu, jos sana ei puussa
        for child in n_gram:
            if child not in current_node.children:
                current_node.children[child] = TrieNode()
            current_node = current_node.children[child]

        #n-grammin/sekvenssin lopuksi merkitään sana päättyneeksi is_end_of_sequence=True
        current_node.is_end_of_sequence = True

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

    def trie_getter(self, sequence):
        """hakusekvenssi mielivaltainen - tallennetaan annetun sekvenssin seuraajat frekvensseineen 
        tupleen listoina ([seuraajat], [seuraajien frekvenssit])"""
        next_frequencies = ([],[])
        return next_frequencies

    def generate(self, sequencies_frequencies, length):
        #Generoidaan seuraavat sanat painotetulla arvontafunktiollas
        sequencies = sequencies_frequencies[0]
        frequencies = sequencies_frequencies[1]
        if len(length) == 0:
            return  
        new_sequence = random.choices(sequencies, weights=frequencies, k = length)
        return new_sequence
   
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

