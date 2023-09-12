from os import system
system("cls")
list1 = list(range(3, 13, 3))
#print(list1)

name = "Enrique"
list2 = list(name)
list2 = list([name, "Diego"])
list2.append("Carlos")
print(list2)

print(type(name))
print(type(list2))

for i in list2:
    print(i)
   