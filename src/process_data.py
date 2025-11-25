import re
#haetaan tavutettu aineisto

def process():
    corpus = open("src/data/corpus.txt").read()
    #corpus = re.sub(r"[^a-zA-Z0-9\säöåÄÖå-]", "", corpus)
    #corpus = corpus.lower()
    return corpus
