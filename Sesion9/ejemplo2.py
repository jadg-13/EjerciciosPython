fruits = list()

fruits.append("Mandarina")
fruits.append("Sandía") 
fruits.append("Limón")
fruits.append("Naranja")  
fruits.append("Manzana")

x = fruits.copy()

import os
os.system("cls")
print(x)

fruits.append("Mango")

print(f"Lista de Frutas {fruits}")
print(f"Lista de x: {x}")