
"""haetaan tavutettu aineisto ja 
    prosessoidaan se markovin ketjuun sopivaksi: 
    (sana, tavumäärä:int)"""

def process(path):
    corpus = open(path).read()
    corpus = corpus.replace("\n", " ")
    corpus = corpus.split(" ")
    words = [word for word in corpus[0::2]]
    syllables = [int(syllable) for syllable in corpus[1::2]]
    corpus = list(zip(words, syllables))

    return corpus
