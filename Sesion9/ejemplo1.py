list1 = list()
list2 = list()

list1.append("Diego")
list1.append("Carlos")
list1.append("María")
list1.append("Xochilt")
list1.append("Carolina")

import os 

os.system("cls||clear")
print(list1)
list2.append('Fernando')
print(list2)
list3 = list()
list3 = list1
print(list3)

print("Agregar Managua a la lista")
list1.append("Managua")
print(list1)


print("Agregar Granada a lista 3")
list3.append("Granada")
print("Imprimir listas")
print(f"Lista 3 = {list3}")
print(f"Lista 1 = {list1}")
print(f"Lista 2 = {list2}")

list1 = list2
list2.append(150)
list3.append("Carro")

print("Nuevos valores")
print(f"Lista 1 = {list1}")
print(f"Lista 2 = {list2}")
print(f"Lista 3 = {list3}")

print(type(list1))
print(type(list2))
print(type(list3))