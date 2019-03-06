pilha = []

def push(p, elemento, tipo=str):
    if type(elemento) == tipo:
        p.append(elemento)

def pop(p):
    return p.pop() if len(p) > 0 else None
