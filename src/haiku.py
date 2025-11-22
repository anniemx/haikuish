
class Haiku():
    def __init__(self):
        self.order = 1

    def k_order(self):
        self.order = input("Anna Markovin ketjun aste: ")
        if self.order is None or self.order == "" or int(self.order) < 1 or int(self.order) > 50:
            self.k_order()
        return self.order

    def generate_haiku(self, content):
        #tavut kolmella rivillä 5 - 7 - 5 -> miten saadaan varmistettua oikea tavumäärä?
        #yksi haku 17 tavulle, mutta miten jako-  vai tarkastetaanko jokaisessa haun välissä määrä?

        haiku = []
        haiku_poem = []
        line_no = 1
        count = 0
        for i in range(len(content)):
            haiku_syllables = content[i][0].split("-")
            count += len(haiku_syllables)
        if count == 17: #tarkastetaan, että koko runo on 17 tavua
            line_no = 1 #tarkastetaan rivien tavut
            for i in range(len(content)):
                haiku_poem.append(content[i][0].replace("-", ""))
                self._check_syllables(content, line_no)
                line_no+=1


            print(haiku_poem)
            return True
        return False

    def _check_syllables(self, content, line_no): #rivin tarkastaja helper
        count = 0
        for i in range():
            haiku_syllables = content[i][0].split("-")
            count += len(haiku_syllables)
        if line_no == 2:
            if count == 7:
                return True
        else:
            if count == 5:
                return True
            return False


    def print_haiku(self, haiku_poem):
        #tulosta rivi kerrallaan
        for line in haiku_poem:
            print(line)
