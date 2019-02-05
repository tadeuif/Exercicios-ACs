lista = []
nomes = 0
while nomes != '@':
    nomes = input("Digite os nomes dos familiares: ")
    lista.append(nomes)

print(lista)
print(len(lista))

#i = 0

#for l in lista[i]:
#    print(len(l))

max_tamanho = 0
for i,nome in enumerate(lista): #DEVOLVE INDICE E ELEMENTO
    if len(nome) > max_tamanho:
        max_tamanho = len(nome)
        max_nome = nome
        max_i = i
print("Maior nome: %s, com %d letras, na posição %d"%(max_nome, max_tamanho, max_i+1))
