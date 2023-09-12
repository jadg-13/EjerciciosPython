name = "Jezer"
list1 = list(name)
list2 = list([list1, "Freddy"])
list3 = list([list2, "Jesus"])

for elemento in list3:
    for subelemento in elemento:
        print(subelemento)

