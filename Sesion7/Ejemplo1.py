from os import system
system("cls||clear")
list1 = list([1, 2, 3, 4, 5, "Diego"])
list2 = [1, "Carlos"]
list3 = {1, 2, 4, "Enrique"}
name = "1, 2, 3, Richard"
print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(name, type(name))
print("Lista 1")
for i in list1:
    print(i)
print("lista set 3")
for i in list3:
    print(i)



for i in list2:
    print(i)
for letra in name:
    print(letra)
