from clases import Student
from os import system

system("cls || clear")
#Agregar elementos en diccionario
students = {1: Student("Carlos", "talavera@gmail.com", "ISI", 90, 500)}


students2 = dict( est1 = Student("Diego", "diego@gmail.com", "ISI", 100, 600))

#Imprimir diccionarios
print(students)
print(students2)

#mostrar valores del diccionario
print(students2["est1"])
print(students[1])