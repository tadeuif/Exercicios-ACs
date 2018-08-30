def criarlist():
    inputlista= 0
    lista=[]   
    while inputlista != "":
        if inputlista=="":
            break
        else:
            inputlista=input("Digite um item para ser adicionado a lista:")
            lista.append(inputlista)
            tamanho= len(lista)-1
            
            
    del lista[tamanho]         
    print(lista)
    print("Quantidade de items no carrinho:",len(lista))
    return lista


def main():
    criarlist()




