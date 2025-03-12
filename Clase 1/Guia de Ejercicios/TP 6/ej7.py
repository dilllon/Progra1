#Calcular y devolver el máximo comun divisor de dos enteros no negativos basándose en las siguientes formulas matemáticas
#MCD(X,X) = X
#MCD(X,Y) = MCD(Y,X)
#Si X > Y => MCD(X, Y) = MCD(X-Y, Y)
#Ejemplo: MCD(40, 15) devuelve 5

def calcularMCD(n1, n2):
    while n1 != n2:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    return n1


def main():
    n1 = int(input("Ingrese el primer valor: "))
    while n1 <= 0:
        print("Ingrese un número válido. ")
        n1 = int(input("Ingrese el primer valor: "))
    
    n2 = int(input("Ingrese el segundo valor: "))
    while n1 <= 0:
        print("Ingrese un número válido. ")
        n2 = int(input("Ingrese el segundo valor: "))

    resultado = calcularMCD(n1, n2)
    print("El MCD de ", n1, "y ", n2, "es: ", resultado)

main()