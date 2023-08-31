"""Adivina el numero"""
import random
import os
os.system("cls||clear")
num = random.randint(1, 10)

adivino = False
oportunidades = 3
while (oportunidades > 0) and (adivino == False):
    print("Dime un # ")
    x = int(input())
    if(x == num):
        adivino = True
        print("Adivinaste")
        break
    else:
        print(f"Sigue intentando te quedan {oportunidades}")
    oportunidades-=1