#Imprimir una columna de asteriscos, donde su altura se recibe como parámetro

def construirColumna(n):
    for i in range(n):
        print("*")
    return


def main():
    n = int(input("Ingrese la altura de la columna: "))
    construirColumna(n)

main()