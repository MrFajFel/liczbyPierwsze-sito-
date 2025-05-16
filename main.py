#dziala
class Sito:

    def __init__(self,n):
        self.n = n
        self.pierwsze = [True for i in range(n+1)]

    def generuj(self):
        for i in range(2,int(self.n ** 0.5)+1):
            if self.pierwsze[i]:
                w = i*2
                while w <= self.n:
                    self.pierwsze[w] = False
                    w += i

    def wyswietl(self):
        for i in range(2,self.n+1):
            if self.pierwsze[i]:
                print(i, end=" ")




sito = Sito(10000)
sito.generuj()
sito.wyswietl()
