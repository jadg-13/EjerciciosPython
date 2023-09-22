miPila = list()
otraPila = list()

def apilar(nombre):
    miPila.append(nombre)

def desapila():
    book = miPila.pop()
    otraPila.append(book)
    return book 

apilar("Sofía del Sofía de los Presagios")
apilar("Historia de una muerte anunciada")
apilar("El principito")
apilar("Cien años de soledad")
apilar("El alquimista")
apilar("Romeo y Julieta")
apilar("Azul")
apilar("La metaforsis")
apilar("Job")

cont = len(miPila)
while cont > 0:
    print(desapila())
    cont-=1

print(otraPila)