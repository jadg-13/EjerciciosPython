#suma de un numero con dos digitos

number = int(input("Dime un numero entero: "))
if number >=10 and number <=99:
    first_number = number // 10
    second_number = number % 10
    print("La suma de las cifras es: ", first_number + second_number)
else:
    print("El numero no es de dos cifras")


