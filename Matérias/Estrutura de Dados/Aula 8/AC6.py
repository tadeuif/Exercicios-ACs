#Busca Binária
def busca_binaria(lista, elemento, esquerda=0,direita=0, meio=0):
    direita_len = len(lista) - 1
    meio = (esquerda + direita) // 2
    if len(lista) == 0:
        return None
    if elemento == lista[meio]:
        return lista[meio]
    elif lista[meio] < elemento:
        nova_esquerda = meio + 1
        novo_meio = (esquerda + direita_len) // 2
        return busca_binaria(lista, elemento, esquerda=nova_esquerda, direita=direita_len, meio=novo_meio)
#Quick Sort
def quick_sort(lista):
    pass

#Busca em Listas
def busca_em_listas(lista, elemento):
    pass

#Nas funções busca_binaria() e quick_sort(), use um print() para mostrar os elementos visitados, no caso da busca_binaria() será o centro da lista em cada chamada da função e no caso do quick_sort() será o primeiro elemento da lista em cada chamada da função.

l1 = [0,1,2,3,4,5,6,7,8,9]
print(busca_binaria(l1, 8))