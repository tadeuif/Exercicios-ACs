def verifica_ordenacao(lista):
    lenght = len(lista)
    ind_2 = 1
    for i in range(lenght):
        if ind_2 < lenght:
            if lista[i] > lista[ind_2]:
                return False
            else:    
                ind_2 += 1
    else:
        return True

lista = [0,1,2,3,4,5,6,7,8]
print(verifica_ordenacao(lista))

def busca(lista, elemento_desejado):
    for i in lista:
        if elemento_desejado == lista[i]:
            return i
    return None

print(busca(lista, 9))
"""Busca linear que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None"""
    


def busca_binaria(lista, elemento_desejado):
    tamanho_total = len(lista)
    elemento_central = tamanho_total / 2
    if lista[elemento_central] == elemento_desejado:
        return elemento_central
    for elemento_central in lista:
        if elemento_desejado > lista[elemento_central]:
            elemento_central += 1
    return None

print(busca_binaria(lista, 9))
        


"""Busca binária que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None"""
    


#def busca_binaria_strings(lista, elemento_desejado):
"""Busca binária com uma lista de strings que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None. Se a lista não estiver ordenada, também retorna None"""
    #pass'''