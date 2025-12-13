
class Haiku():
    def __init__(self):
        self.order = 1

    def k_order(self):
        self.order = input("Anna Markovin ketjun aste: ")
        if self.order is None or self.order == "" or int(self.order) < 1 or int(self.order) > 50:
            self.k_order()
        return self.order

    def print_haiku(self, haiku_poem):
        #tulosta rivi kerrallaan
        for line in haiku_poem:
            line[:] = [word[0].replace(".", "") for word_list in line for word in word_list]
            print(line)