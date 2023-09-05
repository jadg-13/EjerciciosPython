import os
from math import *

def calcAreaCirc(radio):
    return round(pi * pow(radio, 2), 4)

def menu():
    op = 0
    while(op!=4):
        os.system("cls")
        print("Sesión 04/09/2023")
        
        message = """1. Calcular el area de un circulo
2. Calcular el cubo de un numero
3. Calcular la raiz cuadrada de un numero
4. Salir
Digita tu opcion: """
        print(message)
        op = int(input())
        if(op == 1):
            r = float(input("Dime el radio: "))
            print(f"El area circulo es {calcAreaCirc(r)}")
        elif(op == 2):
            n = int(input("Dime un número: "))
            print(f"El cubo es : {pow(n, 3)}")
        elif(op == 3):
            n = int(input("Dime un número: "))
            print(f"La raiz cuadrada es: {sqrt(n)}")
        elif(op==4):
            print("Adios...")
        else:
            print("Opción invalida...")
        os.system("pause")

def main():
    
    #menu()

if __name__== '__main__':
    main()
