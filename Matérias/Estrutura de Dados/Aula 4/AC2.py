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
    for c in lista:
        if c == "(" or c == ")" or c == "[" or c == "]" or c == "{" or c == "}":
            push(pilha, c)
        else:
            pass

    if pilha == pilha[::-1]: #Não é isso!
        return True
    else:
        return False 

print(balanceada('(1234)'))
