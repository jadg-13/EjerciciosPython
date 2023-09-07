# Leer un listado de frutas y solo mostrar las frutas cuyo nombre tenga mas de 5 letras
frutas = list()


def agregar():
    fruta = input("Dime el nombre de la fruta: ")
    frutas.append(fruta)

def imprimir():
    for fruta in frutas:
        if len(fruta)>5:
            print(fruta)
def main():
    op = 0
    while op != 3:
        op = int(
            input("""MENU
1. Agregar
2. Mostrar 
3. Salir
Digite la Opcion: """)
    )
        if(op == 1):
            agregar()
        elif(op ==2):
            imprimir()
        else:
            print("Adios")

main()

