'''
Tadeu Inocencio Freitas - RA 1800250
Tibério Cruz - RA 1800110
Vinícius Motta - RA 1800842

'''
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

lista3 = [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142,144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]
print(verifica_ordenacao(lista3))

'''def busca(lista, elemento_desejado):
    for i in lista:
        if elemento_desejado == lista[i]:
            return i
    return None'''

'''print(busca(lista3, 122))'''

def busca_binaria(lista, elemento_desejado):
    indice_inicial = 0
    indice_final = len(lista)
    while indice_inicial < indice_final:
        meio = indice_inicial + (indice_final - indice_inicial) // 2
        valor = lista[meio]
        if elemento_desejado == valor:
            return meio
        
        elif elemento_desejado > valor: #Se valor estiver a direita, está condição vai atender aos elementos da esquerda
            if indice_inicial == meio: #Condição de parada do looping caso o valor não for encontrado  
                return None  
            indice_inicial = meio #Afunila a pesquisa não danificando a lista inicial
        
        elif elemento_desejado < valor:#Se valor estiver a esquerda, está condição vai atender aos elementos da esquerda
            indice_final = meio#Afunila a pesquisa não danificando a lista inicial
lista=[1,2,3,4,5,6,7,8]
print(busca_binaria(lista3,122))

def busca_binaria_strings(lista, elemento_desejado):
    if verifica_ordenacao(lista) == True:
        pass
    else:
        return None
    indice_inicial = 0
    indice_final = len(lista)
    while indice_inicial < indice_final:
        meio = indice_inicial + (indice_final - indice_inicial) // 2
        valor = lista[meio]
        if elemento_desejado == valor:
            return meio
        
        elif elemento_desejado > valor: #Se valor estiver a direita, está condição vai atender aos elementos da esquerda
            if indice_inicial == meio: #Condição de parada do looping caso o valor não for encontrado  
                return None  
            indice_inicial = meio #Afunila a pesquisa não danificando a lista inicial
        
        elif elemento_desejado < valor:#Se valor estiver a direita, está condição vai atender aos elementos da esquerda
            indice_final = meio#Afunila a pesquisa não danificando a lista inicial

lista2=[1,4,3,4,5,6]
lista2=['adde','bee','c','d']
print(busca_binaria_strings(lista2,'c'))