#Introduccion a listas.
lista = list()
print(lista)
lista.append(1)
print(lista)
lista.append("Diego")
print(lista)
lista.append(99.99)
print(lista)
#imprimir elementos con while
cont = 0
while(cont < len(lista)):
    print(cont, lista[cont])
    cont+=1

#Imprimir elementos con for
for item in lista:
    print(item)