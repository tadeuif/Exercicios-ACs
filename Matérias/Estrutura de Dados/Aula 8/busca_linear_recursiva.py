def busca_linear_recursiva(lista, elemento, indice=0):
    if len(lista) == 0:
        return None
    elif lista[0] == elemento:
        return indice
    else:
        return busca_linear_recursiva(lista[1:], elemento, indice + 1)

if __name__ == 'main':
    l1 = [10,34,12,17,2,90,15]
    e = 2

    posicao = busca_linear_recursiva(l1, e)