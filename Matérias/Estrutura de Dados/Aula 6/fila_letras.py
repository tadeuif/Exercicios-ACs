def enqueue(fila, elemento):
    fila.append(elemento)

def dequeue(fila):
    return fila.pop(0)

dados_ord = [chr(ord('a')+i) for i in range(26)]

def desorganizar_dados(dados):
    dados_desord = []
    tam = len(dados) - 1
    for i in dados:    
        ult = dados[tam]
        if i in dados_desord or ult in dados_desord:
            pass
        else: 
            dados_desord.append(i)
            dados_desord.append(ult)
            tam -= 1
    return dados_desord

def criar_fila(dados): 
    fila = []
    tam_lista = len(dados)
    for i in range(tam_lista):
        enqueue(fila, dados[i])
    return fila

def ultimos(fila, p):
    tam_fila_real = len(fila)
    tam_fila_solicitado = p
    fila_original = [] #2 ideia sem perder a fila original
    fila_original.extend(fila) #2 ideia sem perder a fila original
    while tam_fila_real > tam_fila_solicitado:
        #fila_original.append(fila[0]) 1 ideia
        dequeue(fila)
        tam_fila_real = len(fila)
    #fila.extend(fila_original) 1 ideia
    return fila, fila_original

def Main():
    lista_desorganizada = desorganizar_dados(dados_ord)
    fila = criar_fila(lista_desorganizada)
    print(ultimos(fila, 3))
Main()