pilha = []

def push(p, elemento, tipo=str):
    if type(elemento) == tipo:
        p.append(elemento)

def pop(p):
    return p.pop() if len(p) > 0 else None

def len(p):
    return len(p)

s = 'arara'
lista = list(s)

for c in lista:
    push(pilha, c)

def palindromo(pilha):
    
    if pilha == pilha[::-1]:
        return True
    else:
        return False       

print(palindromo(pilha))