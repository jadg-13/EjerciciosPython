matriz = [[2, 30, 1209], 
          [5, 6000, 234],
          [234, 1232, 95962],
          [23234, 3432, 1223],
          ["cafe", "Gaseosa", "leche"],
          [[1, 3, 3], ["juan", "pedro"], 12],
          [[1,2,3],
           ["juan", 0, 2], 
           [3, 4], ["sofia", 3]]
          ]
import os 
os.system("cls|| clr")

i = 0
for fila in matriz:
    for columna in fila:
        print(f"{columna}", end = " |")   
    print("")

"""
for fila in matriz:
    for columna in fila:
        print(f"{columna:>9}", end=" ")
    print("")    
"""