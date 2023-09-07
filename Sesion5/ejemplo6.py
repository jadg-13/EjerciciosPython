# Leer x cantidad de numeros reales y mostrar la raiz cuadrada de cada numeros.

numeros = list()

num = 1

while(num != 0):
    num = eval(input("Dime un numero: "))
    numeros.append(num)

from math import sqrt
for num in numeros:
    print(f"{num}, Raiz cuadrada: {sqrt(num)}")