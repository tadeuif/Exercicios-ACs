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

lista3 = [0,1,2,3,4,5,6,7,8]
print(verifica_ordenacao(lista3))

def busca(lista, elemento_desejado):
    for i in lista:
        if elemento_desejado == lista[i]:
            return i
    return None

print(busca(lista3, 9))

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
print('O elemento 2 na lista ',lista,'está na posição ',busca_binaria(lista,2))

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
print('O elemento c na lista ',lista2,'está na posição ',busca_binaria_strings(lista2,'c'))