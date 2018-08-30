def exibeMsg():
    print("Para converter o grau de Célsius para Fahrenheit ou vice-versa, digite C ou F")

def getConvertTo():
    y = input("Digite o tipo de conversão: F ou C: ")
    return y

def exibeFahrenheitToCelsius(start, end):
    start = float(input("Digite o primeiro valor de Fahrenheit:" ))
    end = float(input("Digite o segundo valor de Fahrenheit:" ))
    while start <= end:
        c = (start-32) * 5 / 9
        print("Valor convertido em Célsius: %dº C" %c, "%4.fº F"%start)
        start = start + 1
        
def exibeCelsiusToFahrenheit(start2, end2):
    start2 = float(input("Digite o primeiro valor de Célsius:" ))
    end2 = float(input("Digite o segundo valor de Célsius:" ))
    while start2 <= end2:
        f = (start2 * 9 / 5) + 32
        print("Valor convertido em Fahrenheit:%4.fº F" %f, "%dº C" %start2)
        start2 = start2 + 1




def Main():
    
    exibeMsg()
    conver2 = getConvertTo()
    
    if conver2 == "C" or conver2 == "c":
        exibeCelsiusToFahrenheit(0,999)
    elif conver2 == "F" or conver2 == "f":
        exibeFahrenheitToCelsius(0,999)
    
    
Main()
