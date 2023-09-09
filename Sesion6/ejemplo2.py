#Leer x cantidad de numeros e imprimir la lista ordenada.
import os
os.system("cls")
numbers = list()

import random
numbers = [random.randint(0, 100) for i in range(30)]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)
print(numbers)