import itertools
from os import system

def permutaciones(palabra):
    letras = list(palabra)
    todas_permutaciones = list(itertools.permutations(letras))
    i = 1
    for permutacion in todas_permutaciones:
        palabra_permutada = ''.join(permutacion)
        print(f"Combinación: {str(i):>6}: {palabra_permutada}")
        i+=1

# Permutar
system("cls||clear")

palabra = input("Escribe una palabra: ")
permutaciones(palabra)
