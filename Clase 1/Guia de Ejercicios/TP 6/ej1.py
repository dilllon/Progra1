#Escribir una funcion que reciba como parámetros dos números enteros. Calcular y devolver el resultado de la multiplicación de ambos valores utilizando solamente sumas.
#Por ejemplo: 4*3 = 4 + 4 + 4


def multiplicarEnteros(num1, num2):
    aux = 0
    for i in range(num1):
        aux += num2
    return aux

def main():
    num1 = int(input("Ingrese el primer valor a multiplicar: "))
    num2 = int(input("Ingrese el segundo valor a multiplicar: "))
    producto = multiplicarEnteros(num1, num2)
    print("El producto es: ", producto)

main()