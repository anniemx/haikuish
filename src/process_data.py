
"""fetch data and process for trie as a list of 
    sentences [(word, syllable_count:int),...]"""

def process(path):
    data = open(path, encoding="utf-8").read()
    data = data.split("\n")
    corpus = []

    for line in data:
        all_words = line.split(" ")
        sentence = []
        for word in all_words:
            word_syllables = word.split(":")
            word = (word_syllables[0], word_syllables[1])
            sentence.append(word)
        corpus.append(sentence)

    return corpus


if __name__ == "__main__":
    corpus1 = process(path = "src/data/corpus_syllables.txt")