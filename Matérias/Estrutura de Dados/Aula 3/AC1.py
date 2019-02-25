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

def verifica_circular(seq):
    it = 0
    it2 = 1
    indtup = 0
    il = 0
    il2 = 1
    lenght = len(seq) - 1
    peca3 = Domino(0,0)
    for i in range(lenght):
        peca1 = Domino(seq[il][it],seq[il][it2])
        peca2 = Domino(seq[il2][it],seq[il2][it2])
        if peca1.connecta(peca2):
            if indtup < 1:
                peca3 = peca1
                seq[indtup]
                indtup += 1
                il += 1
                il2 += 1
            else:
                seq[indtup]
                indtup += 1
                il += 1
                il2 += 1
        else:
            return False
    if peca2.connecta(peca3):
        return True
    else:
        return False

def verifica_repetidas(seq):
    lenght = len(seq) - 1
    indtup = 0
    indtup2 = 1
    for i in range(lenght):
        if indtup < indtup2:
            for indlista in range(lenght):
                if seq[indtup] == seq[indtup2]:
                    return True
                else:
                    indtup2 += 1
        indtup += 1
        indtup2 = indtup + 1
        lenght -= 1
    return False

pecas = ler_arquivo_todo('domino.dat')
print(pecas)
print(verifica_sequencia(pecas))
print(verifica_circular(pecas))
print(verifica_repetidas(pecas))






