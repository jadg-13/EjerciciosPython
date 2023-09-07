#Leer x cantidad numeros pares y mostrar dichos numeros
lista = list()

def esPar(num):
    return num % 2 ==0

def main():
    flag = 'Si'
    while flag.lower() != 'No'.lower():
        num = eval(input("Dime un numero: "))
        if(esPar(num)):
            lista.append(num)
        flag = input("Desea ingresar otro numero: Si - No: ")
    
    print("Numeros pares almacenados en la lista.")
    for num in lista:
        print(f"Numero: {num}")

if __name__ == "__main__":
    main()
