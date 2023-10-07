#1. Almacenar en un diccionario los nombres y notas de los alumnos de un curso.
students = dict(Diego = 10, Enrique = 10, Carlos = 10, Cesar=6, Luis=7, Pedro=8, Juan=9, Jose=10,)
#2. Imprimir la lista de alumnos con su respectiva nota.
#print(students)
#for student in students:
#    print(student, students[student])
for nombre, nota in students.items():
    print(f"Estudiante: {nombre:<10}, Nota: {nota:>3}")

#3. Imprimir los alumnos cuya nota sea mayor que 7.
# for name, grade in students.items():
#     if grade > 7:
#         print(name, grade)
