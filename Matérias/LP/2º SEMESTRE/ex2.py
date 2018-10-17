def fib(n):
    a = 1
    b = 1
    c = 1
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    return c

def fib2(n):
    a = 1
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return a

def fib3(n):
    a, b = 1, 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return a

def fib4(n):
    a, b = 1, 1
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
    return a

def fib5(n):
    if n <= 2:
        return 1
    else:
        return fib5(n-1) + fib5(n-2)

def fib6(n):
    
    return 1 if n <= 2 else fib5(n-1) + fib5(n-2)
    
def caracteres(s): #QUESTÃO DE PROVA
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def caracteres2(s): #QUESTÃO DE PROVA
    d = {}
    for c in s:
        try:
            d[c] += 1
        except KeyError:
            d[c] = 1
    return d