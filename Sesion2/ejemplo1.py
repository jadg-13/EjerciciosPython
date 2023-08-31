import os
os.system("cls||clear")
print("Bienvenidos a la segunda sesión")
print("="*50)
#declarar variable
nombre = input("Dime tu nombre: ")
print(f"Mucho gusto {nombre}")
anioNac = int(input("En que año naciste "))
edad = 2023 - anioNac
print(f"{nombre} tienes {edad} años.")