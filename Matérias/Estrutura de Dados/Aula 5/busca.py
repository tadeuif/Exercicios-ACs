def verifica_ordenacao(lista):
    lenght = len(lista)
    ind_2 = 1
    for i in range(lenght):
        if i+1 <= lenght:
            if lista[i] < lista[ind_2]:
                ind_2 += 1
                return False
        else:    
            if lista[i-1] < lista[i]:
                return False
    else:
        return True

lista = [0,1,2,3,4,5,6,8,7]
print(verifica_ordenacao(lista))
'''def busca(lista, elemento_desejado):
"""Busca linear que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None"""
    pass


def busca_binaria(lista, elemento_desejado):
"""Busca binária que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None"""
    pass


def busca_binaria_strings(lista, elemento_desejado):
"""Busca binária com uma lista de strings que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None. Se a lista não estiver ordenada, também retorna None"""
    pass'''