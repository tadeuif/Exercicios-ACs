import datetime


zodiacList = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

def inputBirth ():
    
    inputDate = "Datas: "
    listDates = []
    
    while inputDate != -1:
        inputDate = input("Digite a data de aniversário no formato americano 0000/00/00: ")
        day, month, year = map(int, inputDate.split('/'))
        date1 = datetime.date(day, month, year)
        listDates.append(date1)
        lenght = len(listDates)-1

        #if inputDate != "00/00/0000":
            #print("Por favor digite uma data no formato válido")
        #splited = int(inputDate.split('/'))
        #date = datetime.date(splited)
            
    del listDates[lenght]
    
    print(listDates)
    return listDates

#def dateToZodiac ():

    #if num in list1[0]:
        

def Main():

    inputBirth()

Main()
