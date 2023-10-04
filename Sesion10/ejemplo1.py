# Arreglo de numeros 
# Mostrar los numeros pares
# Mostrar las suma de los impares
# Mostar todos los elementos de la lista.
# Buscar un elemento en la lista
# Eliminar un valor

import os 

listNumbers = list()

def addNum():
    num = int(input("Dime un numero: "))
    if(isNumber(num)):
        print(f"El numero {num} ya se encuentra registrado.")
    else:
        listNumbers.append(num)
    os.system("pause")

def showPairs():
    os.system("cls||clear")
    print("Mostrar numeros de numeros pares")
    for number in listNumbers:
        if number % 2 ==0:
            print(number)
    os.system("pause")

def showSumUnPairs():
    suma = 0
    for num in listNumbers:
        if num%2 != 0:
            suma += num
    print(f"Las Suma de los impares es: {suma}")
    os.system("pause")

def showList():
    print(listNumbers)
    os.system("pause")

def searchNumber(number):
    if number in listNumbers:
        print(f"Se encontro {number}")
    else:
        print(f"No se encontro {number}")

def deleteNumber(number):
    if(isNumber(number)):
        listNumbers.remove(number)
        print(f"Se a eliminado el numero: {number} satisfactoriamente")
    else:
        print(f"{number} no existe")
    os.system("pause")

def isNumber(number):
    return number in listNumbers

def menu():
    print("""1. Agregar 
2. Mostrar Pares
3. Mostrar sumas impares
4. Mostrar lista
5. Buscar numero
6. Elininar numero
0. Salir""")
    option = int(input("Digita la opcion: "))
    if(option == 1):
        addNum()
    elif(option == 2):
        showPairs()   
    elif(option == 3):
        showSumUnPairs()
    elif(option == 4):
        showList()
    elif(option ==5):
        number = int(input("Dime un numero: "))
        searchNumber(number=number)
        os.system("pause")
    elif(option == 6):
        num = int(input("Dime el numero que deseas eliminar: "))
        deleteNumber(num)
    elif(option == 0):
        print("Adios...")
    else:
        print("Opción existe")
    return option
    
def main():
    op = -1
    while op != 0:
        os.system("cls")
        op = menu()

main()

