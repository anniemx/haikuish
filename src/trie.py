import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_sequence = False
        self.frequency = 1

    #def __repr__(self):
    #    return f"TrieNode(children={list(self.children.keys())},\
    #    is_end_of_sequence={self.is_end_of_sequence}, frequency={self.frequency})"


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.sequence = []
        self.search_sequence = []
        self.sequence1 = []
        self.sequence2 = []
        self.sequence3 = []
        self.line_limits = {1:5, 2:12, 3:17} #5-7-5: line1 - line2 - line3
        self.line_no = 1
        self.syllable_count = 0

    def __repr__(self):
        return "".join(self._repr_recursive(self.root, ()))

    def _repr_recursive(self, node, word):
        result = []
        result.append(f"Node:{word}, children={list(node.children.keys())}")
        for item, child in node.children.items():
            result.append(self._repr_recursive(child, word + (item, )))
        return "".join(result)

    def trie_insert_markov_chain(self, markov_chain):
        """lisätään n-grammit trie-puuhun sanoittain,
        markovin ketjusta saadaan sekvenssit ja frekvenssit sanakirjana"""

        for n_gram, frequency in markov_chain.items():
            self.trie_insert(n_gram, frequency)

    def trie_insert(self, n_gram, frequency):
        """lisätään sana kerrallaan -> luodaan uusi solmu, jos sana ei ole puussa"""
        current_node = self.root
        for child in n_gram:
            if child not in current_node.children:
                current_node.children[child] = TrieNode()
                current_node.frequency = frequency
            current_node = current_node.children[child]
        #n-grammin (sekvenssin) lopuksi merkitään n-grammi päättyneeksi
        current_node.is_end_of_sequence = True

    #sekvenssin seuraajat frekvensseineen: ([seuraajat], [seuraajien frekvenssit])

    def trie_search(self, sequence):
        """#etsitään trie-puusta sekvenssi, palautetaan true/false"""

        current_node = self.root
        for child in sequence: # käydään läpi sanat sekvenssistä
            if child not in current_node.children:
                #palautetaan False -> sana ei puussa
                return False
            current_node = current_node.children[child]
        return current_node.is_end_of_sequence


    def generate(self, k_order, length):
        """Generoidaan sanoja length-verran. Aloitetaan haku sekvenssistä k=0, 
            eli tyhjästä listasta. Generoidaan halutun k-asteen verran sanoja 
            hakusekvenssiin. Sen jälkeen generoidaan sana kerrallaan seuraajat 
            ja niiden frekvenssit tuplena ([sekvenssit],[frekvenssit]), 
            joista arvotaan koko sanalistaan seuraava sana. Markovin ketjun 
            k-aste tarkastetaan jokaisen generoidun sanan jälkeen ja muokataan 
            hakusekvenssi k-asteiseksi, eli poistetaan ensimmäinen sana."""

        if k_order == 0 or k_order is None or length is None or length == 0:
            return []

        for i in range(length + 1):
            if len(self.search_sequence) < int(k_order):
                next_search_wordlist = self.get_list_words(self.search_sequence)
                next_search_word = random.choices(next_search_wordlist[0],
                                                  weights=next_search_wordlist[1], k = 1)[0]
                print(self.sequence)
                result = self.haiku_format_count(next_search_word, next_search_wordlist)
                if result is True:
                    return self.sequence
                #self.sequence.append(next_search_word)
                #search_sequence.append(next_search_word)

            else:
                if len(self.search_sequence) > int(k_order):
                    self.search_sequence.pop(0)
                next_wordlist = self.get_list_words(self.search_sequence)
                next_search_word = random.choices(next_wordlist[0],
                                           weights=(next_wordlist[1]), k = 1)[0]
                #self.sequence.append(next_word)
                #search_sequence.append(next_word)
                print(self.sequence)
                result = self.haiku_format_count(next_search_word, next_wordlist)
                if result is True:
                    return self.sequence
        
    #tarkastetaan haikumuoto ja tallennetaan listoihin
    def haiku_format_count(self, search_word, wordlist):
        syllables = search_word[1]
        self.syllable_count += syllables
        line_limit = self.line_limits[self.line_no]

        """tarkastetaan ensin sanan pituus: jos generoitu sana liian pitkä, 
        valitaan seuraajalistasta ensimmäinen sopiva:"""
        if self.syllable_count > line_limit:
            for next_word in wordlist[0]:
                next_syllables = next_word[1] #haetaan sanan tavumäärä
                if next_syllables + self.syllable_count - syllables <= line_limit: #lasketaan sopiiko rajaan
                    self.sequence.append(next_word)
                    self.search_sequence.append(next_word)
                    self.syllable_count -= syllables
                    self.syllable_count += next_syllables
                    #return False
                
            #raise ValueError("No found words")
        
        #tarkastetaan haikun tavumäärä riveittän 1:5-2:7-3:5
        elif self.syllable_count < line_limit:
            self.search_sequence.append(search_word)
            if self.line_no == 1:
                self.sequence1.append(search_word)
            elif self.line_no == 2:
                self.sequence2.append(search_word)
            else:
                self.sequence3.append(search_word)
            #return False
        
        #jos rivin tavumäärä täynnä, vaihdetaan rivitieto
        else:
            self.search_sequence.append(search_word)

            if self.line_no == 1:
                self.sequence1.append(search_word)
                self.sequence.append(self.sequence1)
                self.line_no = 2

            elif self.line_no == 2:
                self.sequence2.append(search_word)
                self.sequence.append(self.sequence2)
                self.line_no = 3

            else:
                self.sequence3.append(search_word)
                self.sequence.append(self.sequence3)
                return True
            
            return False


    def get_list_words(self, search_sequence):
        """etsitään seuraajat ja niiden frekvenssit, etsitään siis puusta 
        search_sequence ja lisätään sen k+1 jäsenet ja frekvenssit listaan"""

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