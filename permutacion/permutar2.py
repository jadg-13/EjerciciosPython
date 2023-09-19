
def permutaciones(palabra):
    letras = list(palabra)
    todas_permutaciones = []

    if len(letras) == 0:
        return todas_permutaciones

    permutacion_actual = [''] * len(letras)
    usadas = [False] * len(letras)

    generar_permutaciones(letras, permutacion_actual, usadas, 0, todas_permutaciones)

    i = 1
    for permutacion in todas_permutaciones:
        palabra_permutada = ''.join(permutacion)
        print(f"Palabra # {format(str(i), '0>6')}: {palabra_permutada}")
        i+=1

def generar_permutaciones(letras, permutacion_actual, usadas, nivel, todas_permutaciones):
    if nivel == len(letras):
        todas_permutaciones.append(permutacion_actual.copy())
        return

    for i in range(len(letras)):
        if usadas[i]:
            continue

        permutacion_actual[nivel] = letras[i]
        usadas[i] = True

        generar_permutaciones(letras, permutacion_actual, usadas, nivel + 1, todas_permutaciones)

        usadas[i] = False


def main():
    from os import system
    system("cls || clear")
    palabra = input("Ingresa una palabra: ")
    permutaciones(palabra)

if __name__ == '__main__':
    main()