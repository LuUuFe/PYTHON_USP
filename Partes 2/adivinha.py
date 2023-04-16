import random

class Advinha:
    def __init__(self, quant_num, num):
        self.quant_num = quant_num
        self.num = num

    def le_quant_num(self.quant_num):
        self.quant_num = random.randrange(quant_num)
        
    def verifica(self):
        if self.quant_num == self.num:
            print("Parebens! voçe acertou!!!")
        else:
            print("Infelizmente voçe errou!")
