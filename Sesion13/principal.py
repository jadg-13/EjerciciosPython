from clases import Student
from os import system
import random

students = dict()

def addStudent():
    id = random.randint(100, 999)
    name = input("Nombres: ")
    email = input("Email: ")
    carrer = input("Carrera: ")
    avg = int(input("Promedio: "))
    price = int(input("Precio: "))
    student = Student(name, email, carrer, avg, price)
    students[id] = student

def showStudents():
    for key, value in students.items():
        print(f"""ID: {key}
{value}""")

system("cls")
addStudent()
# addStudent()
# addStudent()

showStudents()


