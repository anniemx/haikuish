import trie

class Haiku():
    def __init__(self):
        self.order = 1

    def k_order(self):
        self.order = input("Anna Markovin ketjun aste: ")
        if self.order == None or self.order == "" or int(self.order) < 1 or int(self.order) > 50:
            self.k_order()
        return self.order

    def generate_haiku(self, content):
        #tavut kolmella rivillä 5 - 7 - 5 -> miten saadaan varmistettua oikea tavumäärä?
        #haku 5 tavulle, haku 7-tavulle, haku 5-tavulle vai yksi haku 17 tavulle?
        haiku = []
        content = [["1-3-2"], ["4-5-6-7-8"], ["9-10-11-12-13-14-15"], ["16-17"]]
        count = 0
        for i in range(len(content)):
            haiku_syllables = content[i][0].split("-")
            count += len(haiku_syllables)
        if count == 17:
            for i in range(len(content)):
                haiku.append(content[i][0].replace("-", ""))
            print(haiku)
            return True
        return False

    def print_haiku(self, haiku_poem):
        #tulosta rivi kerrallaan
        for line in haiku_poem:
            print(line)