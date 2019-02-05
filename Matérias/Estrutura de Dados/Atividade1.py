qtd = int(input("Digite a quantidade de elementos: "))

lista = [0,]*qtd

for i in range(qtd):
    lista[i] = int(input("Digite o valor da posição %d: "%i+1))

soma = 0
#forma1
#soma_str = ''

for i in lista:
    soma += i
    #soma_str += srt(i)+'+'

#soma_str = soma_str[:-1] 
soma_str = str(lista)[1:-1].replace(', ','+')

print("A soma %s resulta em %d" %(soma_str, soma))