import re
from finnsyll import FinnSyll
f = FinnSyll()
#split_compounds=True


def process(batchsize = 1000):
    corpus_words = []
    with open("corpus2.txt", "w", encoding="utf-8") as f:
        for batch in process_batch("ylenews_fi_2018_s.vrt"):
            corpus_words.extend(batch)
            batch = [str(word) for words in batch for word in words]
            f.write(" ".join(batch) + "\n")


def process_batch(file, batchsize = 1000):
    with open(file, "r", encoding="utf-8") as corpus:
        batch = []
        for line in corpus:
            line = line.strip()
            if not line or line.startswith("<"):
                continue
            columns = line.split("\t")
            word = columns[0].lower()
            word = re.sub(r"[^a-zA-Z0-9\säöåÄÖå-]", "", word)
            if word != "":
                word = f.syllabify(word)
                syllables = int(len(word[0].split(".")))
                batch.append((word[0], syllables))
            if len(batch) == batchsize:
                yield batch  
                batch = []
        if batch:
            yield batch


if __name__ == "__main__":
    process()