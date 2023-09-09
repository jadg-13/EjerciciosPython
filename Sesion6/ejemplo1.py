#Funciones 
import os
os.system("cls")
name = input("Dime tu nombre: ")
"""print(f"Tu nombre en mayuscula es: {name.upper()}")
print(f"Tu nombre en minuscula es: {name.lower()}")
print(f"Tu nombre con la primera letra en mayuscula es {name.capitalize()}")
print(f"Quitar espacio {name.strip()}.")
print(f"Reemplazar {name.replace(' ', '')}")
"""

"""
print(f"Reemplazar vocales {name.replace('a', '*')}")
print(f"Reemplazar vocales {name.replace('o', '*')}")
newName = name.replace('a', '*')
newName = newName.replace('o', '*')"""
cont = 0
newName=""
print("Voy a evaluar ")
#while cont < len(name):
    #if(cont == 0): newName = name.replace('a', '*')
newName = name.replace('a', '*')
newName = newName.replace('e', '*')
newName = newName.replace('i', '*')
newName = newName.replace('o', '*')
newName = newName.replace('u', '*')
#    cont+=1

print(f"Nuevo nombre {newName}")


 