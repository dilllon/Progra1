#mucho texto

def calcularRaiz(n):
    a = n/2
    b = 0
    while (a - b) > 0.0001:
        b = ((n/a) + a)/2
        a = ((n/b) + b)/2
    return a



def main():
    n = 0
    while n <= 0:
        n = int(input("Ingresar un número positivo: "))

    resultado = calcularRaiz(n)

    print("La raiz cuadrada aproximada de ese numero es: ", resultado)

main()