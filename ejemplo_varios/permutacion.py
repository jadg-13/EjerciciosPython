#cuantos numero 6 hay en un lista de 1536 numeros
def permutacion(lista):
    lista2=[]
    for i in range(len(lista)):
        if lista[i]==6:
            lista2.append(lista[i])
    return lista2