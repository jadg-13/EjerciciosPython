def obtener_entrada(mensaje):
    return float(input(mensaje))

def calcular_area(base, altura):
    return (base * altura) / 2

def main():
    base = obtener_entrada("Ingresa la base del triángulo: ")
    altura = obtener_entrada("Ingresa la altura del triángulo: ")

    area = calcular_area(base, altura)

    print("El área del triángulo es:", area)

if __name__ == "__main__":
    main()