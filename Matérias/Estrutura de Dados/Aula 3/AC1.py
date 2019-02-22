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

#NOVAS FUNÇÕES
'''AC1'''

def ler_arquivo_todo(arq):

    pecas = []
    linhas = len_arquivo(arq)
    for i in range(linhas):
        pecas.append(ler_arquivo(arq, i))
    return pecas

def verifica_sequencia(seq):
    it = 0
    it2 = 1
    indtup = 0
    il = 0
    il2 = 1
    lenght = len(seq) - 1
    for i in range(lenght):
        peca1 = Domino(seq[il][it],seq[il][it2])
        peca2 = Domino(seq[il2][it],seq[il2][it2])
        if peca1.connecta(peca2):
            seq[indtup]
            indtup += 1
            il += 1
            il2 += 1
        else:
            return False
    return True


pecas = ler_arquivo_todo('domino.dat')
print(pecas)
print(verifica_sequencia(pecas))

#peca1 = Domino(pecas[0][0],pecas[0][1])
#peca2 = Domino(pecas[1][0],pecas[1][1])
#print(peca1.lado_a())
#print(peca1.lado_b())
#print(peca2.lado_a())
#print(peca2.lado_b())
#print(peca1.connecta(peca2))





