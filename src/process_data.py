import re
#import numpy as np


#haetaan tavutettu aineisto, prosessoidaan teksti käsiteltäväksi
def pre_process():
    corpus = open("src/data/mini_corpus.txt").read()
    corpus = re.sub(r"[^a-zA-Z0-9\säöåÄÖå-]", "", corpus)
    corpus = corpus.lower()
    return corpus



