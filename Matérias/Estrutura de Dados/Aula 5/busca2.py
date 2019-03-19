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
    
        elif elemento_desejado < lista[elemento_central]:
            elemento_final = elemento_central - 1
            elemento_central = int((elemento_inicial + elemento_final) / 2)
            
        else:
            elemento_inicial = elemento_central + 1
            if elemento_desejado > lista[elemento_central]:
                #lista = lista[elemento_central + 1:tamanho_total] #Estou quebrando a lista, mas a lógica correta é manter a lista intacta
                elemento_central = int((elemento_inicial + elemento_final) / 2)

lista2 = [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142,144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]               
print(busca_binaria(lista2, 122))
        


"""Busca binária que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None"""
    


#def busca_binaria_strings(lista, elemento_desejado):
"""Busca binária com uma lista de strings que retorna o índice do elemento desejado se estiver na lista, caso contrário retorna None. Se a lista não estiver ordenada, também retorna None"""
    #pass'''