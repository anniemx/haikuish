import re
#haetaan tavutettu aineisto

def process(path):
    corpus = open(path).read()
    corpus = corpus.split(", ")
    words = [word.strip("'/[/]") for word in corpus[0::2]]
    syllables = [syllable.strip("'") for syllable in corpus[1::2]]
    corpus = list(zip(words, syllables))
    print(corpus)
    return corpus
