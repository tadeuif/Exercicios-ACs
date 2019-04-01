def enqueue(fila, elemento):
    fila.append(elemento)

def dequeue(fila):
    return fila.pop(0)

def josephus(jogadores, p):
    fila = []
    i = 1
    while len(fila) < jogadores: #Colocando os jogadores na fila
        enqueue(fila, i)
        i += 1
    jogadas_realizadas = 0
    tam = len(fila)
    ordem_eliminados = []
    while tam > 1:
        if jogadas_realizadas == p:
            enqueue(ordem_eliminados, fila[0])
            dequeue(fila)
            tam = len(fila)
            jogadas_realizadas = 0
        if jogadas_realizadas < p:
            elemento_inicial = fila[0]
            dequeue(fila)
            enqueue(fila, elemento_inicial)
            jogadas_realizadas += 1
    return "Jogados vencedor: {}".format(fila[0]), "Jogadores eliminados por ordem: {}".format(ordem_eliminados)

print(josephus(5,3))