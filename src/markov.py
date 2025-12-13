
class MarkovModel:
    def __init__(self, k_order, corpus):
        self.k_order = int(k_order)
        self.n_grams = []
        self.words = []
        self.markov_model = {}
        self.corpus = corpus

    def generate_ngrams(self):
        #jaetaan tekstiaineisto k+1=n ketjuihin (n-grammeihin)
        n = self.k_order + 1
        for i in range(len(self.corpus) - n + 1):
            self.n_grams.append(self.corpus[i : i + n])
        return self.n_grams

    def find_unique_words(self):
        #etsitään yksittäiset sanat tekstistä
        word_list = list(set(self.corpus.split()))
        return word_list

    def build_model(self):
        """Muodostetaan mallin sanakirja self.markov_model. Ensin generoidaan korpuksesta 
            n-grammit ja lasketaan niiden esiintyvyys korpuksessa. Sitten muodostetaan 
            sanakirja: n-grammit (sekvenssit) tuple-avaimena ja frekvenssit arvona. 
            Palautetaan malli TRIE-hakupuuta varten. Huom! alkuperäisestä aineistosta säilyy tuple, 
            jossa (sana, tavumäärä)."""

        self.generate_ngrams()

        self.n_grams = [tuple(n_gram) for n_gram in self.n_grams]
        for n_gram in self.n_grams:
            if n_gram in self.markov_model:
                self.markov_model[n_gram] += 1
            else:
                self.markov_model[n_gram] = 1
        return self.markov_model
