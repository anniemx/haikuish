import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_sequence = False
        self.frequency = 1

    def __repr__(self):
        return f"TrieNode(children={list(self.children.keys())},\
        is_end_of_sequence={self.is_end_of_sequence}, frequency={self.frequency})"


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.sequence = []

    """lisätään n-grammit trie-puuhun sanoittain, 
        markovin ketjusta saadaan sekvenssit ja frekvenssit sanakirjana"""
    def trie_insert_markov_chain(self, markov_chain):
        for n_gram, frequency in markov_chain.items():
           #print(n_gram, frequency)
           self.trie_insert(n_gram, frequency)

    def trie_insert(self, n_gram, frequency):
        current_node = self.root
        #lisätään sana kerrallaan -> luodaan uusi solmu, jos sana ei ole puussa
        for child in n_gram:
            if child not in current_node.children:
                current_node.children[child] = TrieNode()
                current_node.frequency = frequency

            current_node = current_node.children[child]
        #n-grammin (sekvenssin) lopuksi merkitään sana päättyneeksi is_end_of_sequence=True
        current_node.is_end_of_sequence = True
        #print(f"Inserted n-gram {n_gram}, frequency {frequency}", current_node)

    """hakusekvenssi mielivaltainen - tallennetaan annetun sekvenssin seuraajat frekvensseineen 
        tupleen listoina ([seuraajat], [seuraajien frekvenssit])"""

    #etsitään trie-puusta sekvenssi, palautetaan true/false
    def trie_search(self, sequence):
        current_node = self.root

        for child in sequence: # käydään läpi sanat sekvenssistä
            if child not in current_node.children:
                #palautetaan False -> sana ei puussa
                return False 
            current_node = current_node.children[child]

        return current_node.is_end_of_sequence #palautetaan tieto, että saavutettiin sekvenssin loppu


    def generate(self, k_order, length):
        """Generoidaan sanoja length-verran. Aloitetaan haku sekvenssistä k=0, eli tyhjästä listasta.
            Generoidaan halutun k-asteen verran sanoja hakusekvenssiin. Sen jälkeen generoidaan sana kerrallaan
            seuraajat ja niiden frekvenssit tuplena ([sekvenssit],[frekvenssit]), joista arvotaan koko sanalistaan
            seuraava sana. Markovin ketjun k-aste tarkastetaan jokaisen generoidun sanan jälkeen ja muokataan 
            hakusekvenssi k-asteiseksi, eli poistetaan ensimmäinen sana."""

        search_sequence = []

        for i in range(length + 1):
            if len(search_sequence) < len(k_order):
                
                next_search_wordlist = self.get_list_words(search_sequence)
                #print(next_search_wordlist[0], next_search_wordlist[1])
                next_search_word = random.choices(next_search_wordlist[0], weights=next_search_wordlist[1], k = 1)
                search_sequence.append(next_search_word)

            else:
                if len(search_sequence) > int(k_order):
                    search_sequence.pop(0)
                next_wordlist = self.get_list_words(search_sequence)
                #print(next_wordlist[1])
                next_word = random.choices(next_wordlist[0], weights=(next_wordlist[1]), k = 1)
                self.sequence.append(next_word)
                search_sequence.append(next_word)

        return self.sequence

    def get_list_words(self, search_sequence):
        #etsitään seuraajat ja niiden frekvenssit
        #etsitään siis puusta search_sequence ja lisätään sen k+1 jäsenet ja frekvenssit listaan
        current_node = self.root
        index = 0
        next_words = self._dfs(current_node, search_sequence, index)
        words = list(next_words.keys())
        frequencies = list(next_words.values())
        return (words, frequencies)

    def _dfs(self, current_node, search_sequence, index): #syvyyshaku trie
        if index == len(search_sequence):
            results={}
            
            for word, child in current_node.children.items():
                results[word] = child.frequency        
            #print(results)
            return results #palautetaan lapset, kun ollaan käyty koko puu lävitse
        
        next_word = search_sequence[index]
        #print(next_word)

        if isinstance(next_word, list):
            next_word = next_word[0]

        if next_word in current_node.children:
            return self._dfs(current_node.children[next_word], search_sequence, index + 1)
        
        return None
    








#nämä metodit apuna - ei käytössä
    def get_start(self, first_word, k_order):
        """Aloitetaan aineistosta arvotulla ensimmäisellä sanalla.
        Etsitään sitä seuraavat sanat trie_starts_with() ja arvotaan seuraaja 
        painotetulla arvontafunktiolla. Toistetaan k kertaa, jotta saadaan aste"""
        sequence = []
        word = first_word
        for i in range(k_order):
            self.trie_starts_with(word)

        """sequencies = sequencies_frequencies[0]
        #frequencies = sequencies_frequencies[1]
        #if len(k_order) == 0:
        #    return
        #new_sequence = random.choices(sequencies, weights=frequencies, k = 1)
        #return new_sequence"""

    def trie_starts_with(self, start):
        sequence = start
        current_node = self.root
        for word in sequence:
            if word not in current_node.children:
                return []
            current_node = current_node.children[word]

        next_words = self.get_list_words(current_node, sequence)
        return next_words

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