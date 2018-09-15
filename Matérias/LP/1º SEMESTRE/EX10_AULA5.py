#EX10
bin2 = ""
valido=False
while not valido:
    n1 = int(input("Digite um número inteiro e positivo: "))
    if n1 >= 0:
        valido=True
        
result = n1
while result != 0:
   resto = result%2
   bin2 = bin2 + str(resto)
   result = result // 2
   
print("O número %d em binário = %s" % (n1, bin2[::-1]))

               
