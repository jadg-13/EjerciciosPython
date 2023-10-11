import clases as c
from os import system

listPerson = list()

# Agregar un elemento a la lista
def addPerson():
    fName = input("Ingrese el nombre: ")
    sName = input("Ingrese el apellido: ")
    birt = int(input("Ingrese el año de nacimiento "))
    person = c.Person(fName, sName, birt)
    listPerson.append(person)

# Mostrar todos los elementos de la lista
def showAll():
    for item in listPerson:
        print(f"Nombre: {item.firstName} {item.secondName}")
        print(f"Edad: {item.getAge()}")
        print(f"Email: {item.getEmail()}")
        print(f"{item.isAdult()}")

def main():
    while True:
        system("cls||clear")
        print("1. Agregar persona")
        print("2. Mostrar personas")
        print("3. Salir")
        op = input("Ingrese una opcion: ")
        if op == "1":
            addPerson()
            system("pause")
        elif op == "2":
            showAll()
            system("pause")
        elif op == "3":
            break
        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    main()
