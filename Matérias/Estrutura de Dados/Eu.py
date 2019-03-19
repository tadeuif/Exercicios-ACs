lista = []
def acres(lista, valor):
    while valor <= 200:
        lista.append(valor)
        valor += 2
    return lista

print(acres(lista, 100))