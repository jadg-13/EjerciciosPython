#Dado un numero del 1 al 7, diga el dia de la semana que le corresponde
dias ={1:"Domingo", 2: "Lunes", 3:"Martes", 4:"Miercoles", 5:"Jueves", 6:"Viernes", 7:"Sabado"}

import os
os.system("cls||clear")
dia = int(input("Ingrese un numero del 1 al 7: "))
print(dias[dia])
#actualizando un valor
dias[1]="Sunday"
print(dias)
#agregando un valor
dias[8]="Dia no existe"
print(dias)
#eliminar un valor
dia = int(input("Ingrese un numero del 1 al 7: "))
del dias[dia]
print(dias)