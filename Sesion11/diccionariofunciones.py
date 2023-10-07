#Almacenar productos con su precios en un diccionario.
#Mostrar el siguiente menu:
#1. Agregar Producto
#2. Eliminar Producto
#3. Mostrar Producto
#4. Mostrar todos los productos
#5. Salir
#Utilice funciones.

products = {}

def addProduct():
    name = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    products[name] = price

def deleteProduct():
    name = input("Ingrese el nombre del producto: ")
    if name in products:
        del products[name]
    else:
        print("El producto no existe")

def showProduct():
    name = input("Ingrese el nombre del producto: ")
    if name in products:
        print(f"El precio del producto es: {products[name]}")
    else:
        print("El producto no existe")

def showAllProducts():
    for name, price in products.items():
        print(f"Producto: {name:<10}, Precio: {price:>3}")

def menu():
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Mostrar Producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")
    option = int(input("Ingrese una opcion: "))
    return option

import os
def main():
    while True:
        os.system("cls||clear")
        option = menu()
        if option == 1:
            addProduct()
            os.system("pause")
        elif option == 2:
            deleteProduct()
            os.system("pause")
        elif option == 3:
            showProduct()
            os.system("pause")
        elif option == 4:
            showAllProducts()
            os.system("pause")
        elif option == 5:
            break
        else:
            print("Opcion no valida")
            os.system("pause")
        
if __name__ == "__main__":
    main()