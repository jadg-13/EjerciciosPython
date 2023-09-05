import os
import math

def calcAreaCirc(radio):
    return round(math.pi * pow(radio, 2), 4)

def menu():
    message = """1. Calcular el area de un circulo
2. Calcular el cubo de un numero
3. Calcular la raiz cuadrada de un numero
Digita tu opcion: """
    print(message)
    op = int(input())
    if(op == 1):
        r = float(input("Dime el radio: "))
        print(f"El area circulo es {calcAreaCirc(r)}")
    elif(op == 2):
        n = int(input("Dime un número: "))
        print(f"El cubo es : {pow(n, 3)}")

def main():
    os.system("cls")
    print("Sesión 04/09/2023")
    menu()

if __name__== '__main__':
    main()
