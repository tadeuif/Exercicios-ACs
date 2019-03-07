pilha = []

def push(p, elemento, tipo=str):
    if type(elemento) == tipo:
        p.append(elemento)

def pop(p):
    return p.pop() if len(p) > 0 else None

def lenght(p):
    return len(p)

#s = '(1 + 2)*5', '3*((1*2)+3)'
#lista = list(s)

def palindromo(string):

    lista = list(string)
    for c in lista:
        push(pilha, c)

    if pilha == pilha[::-1]:
        return True
    else:
        return False       

#print(palindromo('arara'))

def balanceada(string):
    lista = list(string)
    virados_esquerda = 0
    virados_direita = 0
    for c in lista:
        if c == "(" or c == ")" or c == "[" or c == "]" or c == "{" or c == "}":
            push(pilha, c)
        else:
            pass
    for c in pilha:
        if c == "(" or c == "[" or c == "{":
            virados_esquerda += 1
        elif  c == ")" or c == "]" or c == "}":
            virados_direita += 1

    if virados_esquerda == virados_direita: 
        return True
    else:
        return False 

print(balanceada('[(1234)]'))
