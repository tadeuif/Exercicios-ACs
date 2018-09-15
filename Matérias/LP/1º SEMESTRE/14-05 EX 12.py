listA = [7, 2, 5, 8, 4]
listB = [2,5,4]

import random

def leInteiroPositivo():
    n=-1
    while n<0:
        n=int(input("Digite um número inteiro:"))
    return n

def geraListaAleatoriosDistintos(n):
    l=[]
    i = 0
    while i < n:
        num = random.randint(1,50)
        if num in l:
            i = i-1
        else:
            l.append(num)
        i = i + 1
    return l

def interseccao(list1, list2):
    list3 = []
    for num in list1:
        if num in list2:
            list3.append(num)
            
    return list3

def union(list1, list2):
    list4 = list1
    for num in list2:
        if num not in list1:
            list4.append(num)
            
    return list4
    

def Main():
    
    l1 = geraListaAleatoriosDistintos(leInteiroPositivo())
    print(l1)
    qtd = leInteiroPositivo()
    l2 = geraListaAleatoriosDistintos(qtd)
    print(l2)
    inter = interseccao(l1, l2)
    print("INTERSECÇÃO: ")
    print(inter)
    uniao = union(l1, l2)
    print("UNIÃO")
    print(uniao)

Main()
        
