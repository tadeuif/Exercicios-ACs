from Ver import len_arquivo
from Ver import ler_arquivo

class Domino:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def verifica(self):
        return type(self.a) == int and\
                type(self.b) == int and\
                0 <= self.a <= 6 and\
                0 <= self.b <=6

    def lado_a(self):
        return self.a

    def lado_b(self):
        return self.b

    def connecta(self, p):
        return p.lado_a() == self.b

    #def verifica_sequencia(self, p):
        #i = 0
        #self.p = p
        #p = []
        #for i in p:
            #p.append(pecas)
            #i += 1
        #return p
def ler_arquivo_todo(arq):

    pecas = []
    linhas = len_arquivo(arq)
    for i in range(linhas):
        pecas.append(ler_arquivo(arq, i))
    return pecas




        

'''AC1'''

#pecas = ler_arquivo('domino.dat', 0)

#print(len_arquivo('domino.dat')
print(ler_arquivo_todo('domino.dat'))

print(ler_arquivo('domino.dat', 0))

#peca1 = Domino(3,4)
#peca2 = Domino(5,4)
#peca3 = Domino(6,4)
#print(peca3.verifica())
#print(peca3.lado_a())
#print(peca3.lado_b())
#print(peca1.connecta(peca2))
#print(peca2.connecta(peca1))

    


