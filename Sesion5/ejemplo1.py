#Uso de variable globales
x = 5

def modificar():
    global x
    x = 3
    x +=1
    print(f"Estoy dentro de la funcion y x es igual a {x}")

print(f"Valor de x antes de entrar a la funcion {x}")
modificar()
print(f"Valor despues de salir {x}")