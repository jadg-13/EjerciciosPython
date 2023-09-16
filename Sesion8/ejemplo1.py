#Deseo una lista de numeros y quiero calcular la media de dichos
from os import system
from statistics import median, mean
numbers = list()

def addNumber(number):
    numbers.append(number)

def readNumber():
    number = int(input("Ingresa un numero: "))
    addNumber(number)

def showNumbers():
    for number in numbers:
        print(number)

#Esta funcion es de peluches (osea primer año) no la voy a usar
def getAverage():
    suma = 0
    for number in numbers:
        suma += number
    avg = suma/len(numbers)
    return avg

#Esta es la tuani
def getAvg():
    return mean(numbers)

def menu():
    op = int(input("""
1. Ingresar
2. Mostrar
3. Media
4. Salir
Dime tu Opcion: 
"""))
    return op
    
def main():
    op = 0
    while(op!=3):
        system("cls||clear")
        op = menu()
        if(op==1):
            readNumber()
            system("pause")
        elif(op==2):
            print("*"*10)
            showNumbers()
            system("pause")
        elif(op==3):
            #print(f"La media es {getAverage()}")
            print(f"La media es {getAvg()}")
            system("pause")
        else:
            print("Gracias por tu visita...")
            system("pause")

main()