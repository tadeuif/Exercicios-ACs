import datetime

zodiacList = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

def inputBirth ():
    
    inputDate = "Datas: "
    listDates = []
    
    while inputDate != -1:
        inputDate = input("Digite a data de aniversário no formato americano 0000/00/00: ")
        if inputDate == "fim":
            inputDate = -1
        else:
            year, month, day = map(int, inputDate.split("/"))
            date1 = datetime.date(year, month, day)
            listDates.append(year)
            lenght = len(listDates)-1

   
    print(listDates)
    return listDates

def dateToZodiac (listDates):
    
    cont = 0
    cont2 = 0
    while listDates[cont2] != -1:
        lenght = len(listDates)-1
        if listDates[cont2] % 12 == cont:
            print(listDates[cont2], "é", zodiacList[cont])
            cont2 = cont2 + 1
            cont = 0
        else:
            cont = cont + 1
            cont2 = cont2
    lenght = len(listDates)-1
        
    del listDates[length]
    
def Main():

    list1 = inputBirth()
    dateToZodiac(list1)

Main()
