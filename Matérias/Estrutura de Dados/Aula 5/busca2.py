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
    tamanho = len(lista)
    tamanho_total = len(lista)
    elemento_central = int(tamanho / 2)
    
    
    for p in lista:
        if lista[elemento_central] == elemento_desejado:
            return elemento_central

        else:
            if elemento_desejado > lista[elemento_central]:
                lista = lista[elemento_central + 1:tamanho_total] #Estou quebrando a lista, mas a lógica correta é manter a lista intacta
                tamanho = len(lista)
                elemento_central = int((tamanho / 2**p-1))
                if lista[elemento_central] == elemento_desejado:
                    return elemento_central
    

print(busca_binaria(lista, 6))
        


"""Busca binária que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None"""
    


#def busca_binaria_strings(lista, elemento_desejado):
"""Busca binária com uma lista de strings que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None. Se a lista não estiver ordenada, também retorna None"""
    #pass'''