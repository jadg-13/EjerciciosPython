#Uso de parametros
# Leer el nombre y el apellido de una persona y mostrar su nombre completo

import os
os.system("cls||clear")
os.system("color a5")

def getFullName(fName, sName):
    return f"{fName} {sName}"

def main():
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    fullName = getFullName(sName=apellido, fName=nombre)
    print(f"El nombre completo es: {fullName}")

if __name__ == "__main__":
    main()
