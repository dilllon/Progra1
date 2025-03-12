#Ej5
#Desarrollar la funcion signo(n) que devuelva 1, -1 o 0 segun el valor recibido sea positivo, negativo o nulo

def signo(n):
    if n == 0:
        return 0
    elif n > 0:
        return 1
    elif n < 0:
        return -1

#Ej6
#Escribir la función comparar(a, b) que reciba como parámetros dos números enteros y devuelva 1 si el primero es amyor que el segundo, 0 si son iguales o -1 si el primero es menor que el segundo.
#En este ejercicio debe aprovecharse la función del ejercicio anterior. Ejemplo comparar(4, 2) devuelve 1, y comparar(2, 4) devuelve -1.

def comparar():
    n1 = int(input("Introduzca el primer valor: "))
    n2 = int(input("Introduzca el segundo valor: "))

    if n1 - n2 == 0:
        return 0
    elif n1 - n2 > 0:
        return n1
    elif n1 - n2 < 0:
        return n2 * -1

def main():
    n = 0
    n = int(input("Ingrese un valor: "))
    print(signo(n))
    n = comparar()
    print(signo(n))

main()

