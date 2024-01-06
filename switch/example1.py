#Decir que dia es de la semana segun el numero ingresado, utilizando match

import os

def showDay(day):
    match day:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
        case _:
            print("Dia invalido")

def main():
    
    day = 0
    while day != -1:
        os.system("clear||cls")
        day = int(input("Ingrese un numero de dia de la semana: "))
        showDay(day)
        input("Presione ENTER para continuar...")
    print("Fin del programa")


if __name__ == "__main__":
    main()
    