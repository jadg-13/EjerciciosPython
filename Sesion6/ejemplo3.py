#Leer un palabra o frase y ocultar las vocales: minusculas, mayusculas, aceptuadas y no acentuadas.
from os import system

system("cls")
system("Color A1")
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó', 'ú']
name = input("Dime una palabra o frase: ")
newName = name
for vocal in vocales:
    newName = newName.replace(vocal, '*')

print(newName)