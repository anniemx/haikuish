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
        haiku = [[content], [], []]
        for line in haiku:
            print(line)

        #haku 5 tavulle, haku 7-tavulle, haku 5-tavulle vai yksi haku 17 tavulle?
        
        return haiku

    def print_haiku(self, haiku_poem):
        #tulosta rivi kerrallaan
        for line in haiku_poem:
            print(line)