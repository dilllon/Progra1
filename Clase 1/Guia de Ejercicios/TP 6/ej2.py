#Dados dos parámetros enteros A y B, obtener A elevado a la B mediante multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar.
#Por ejemplo 4(a la)3 = 4 * 4 * 4

def potenciarEnteros(num1, num2):
    aux = 1
    for i in range(num2):
        aux *= num1
    return aux


def main():
    num1 = int(input("Ingrese el numero a potenciar: "))
    num2 = int(input("Ingrese el numero por el cual sera potenciado: "))
    potencia = potenciarEnteros(num1, num2)
    print("El resultado es: ", potencia)

main()