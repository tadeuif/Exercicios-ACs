lista = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lSecreta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

def translate ():
    inputlist = -2
    listamsg = []
    ind=0
    listFinal = []
    while inputlist != -1:
        inputlist = int(input("Digite a mensagem secreta ou aperte enter para enviar: "))
        listamsg.append(inputlist)
        tamanho = len(listamsg)-1
        
        if inputlist in lSecreta:
            var = inputlist
            #listamsg[var] = lista[var]
            listFinal.append(inputlist)
            
            
            ind=ind+1
        else:
            ind=ind+1
        



        #if inputlist == "":    
         #   listamsg[0] = lista[0]
        
    del listamsg[tamanho]
    


    print(listFinal)
    print(listamsg)
    
    return listamsg
    return listFinal
def Main():

    translate()

Main()
