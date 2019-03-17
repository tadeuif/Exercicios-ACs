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
    elemento_inicial = 0
    elemento_final = lista[-1]
    elemento_central = int(tamanho / 2)
    
    for p in range(elemento_inicial, elemento_final):
        if lista[elemento_central] == elemento_desejado:
            return elemento_central
        else:
            elemento_inicial = elemento_central + 1
            if elemento_desejado > lista[elemento_central]:
                #lista = lista[elemento_central + 1:tamanho_total] #Estou quebrando a lista, mas a lógica correta é manter a lista intacta
                elemento_central = int((elemento_inicial + elemento_final) / 2)
                
print(busca_binaria(lista, 7))
        


"""Busca binária que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None"""
    


#def busca_binaria_strings(lista, elemento_desejado):
"""Busca binária com uma lista de strings que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None. Se a lista não estiver ordenada, também retorna None"""
    #pass'''