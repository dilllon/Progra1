#Desarrollar cada una de las siguientes funciones y escribir un programa principal que permita verificar el funcionamiento de las mismas 
#-Cargar una lista con unmeros al azar de cuatro digitos. La cantidad de elementos también debe ser ignresado por el usuario
#-Calcular y devolver el producto de todos los elementos de la lista
#-Eliminar todas las apariciones de un elemento de la lista. No utilizar listas auxiliares. El elemenot a eliminar se recibe por teclado
#Determinar si una lista es capicua

import random


def agregarNumeros(cant):
    listaRandom = []
    for i in range(cant):
        n = random.randint(1000,9999)
        listaRandom.append(n)
    return listaRandom


def calcularProducto(lista):
    producto = 1
    for i in range(len(lista)):
        aux = lista[i]
        producto *= aux
    return producto


def borrarNumero(lista, numBorrar):
    if numBorrar not in lista:
        print("El número introducido no esta en la lista.")
        return lista
    else:
        while numBorrar in lista:
            lista.remove(numBorrar)
        return lista

#listab = [1000, 1000, 2323] lista de prueba para probar si eliminaba elementos repetidos

def comprobarCapicua(lista):
    n = len(lista)
    for i in range(n // 2): #recorre hasta la mitad de la lista
        if lista[i] != lista[n -1 -i]: #recorre hasta la mitad de la lista a la inversa y compara si son diferentes con el anterior recorrido
            return False
    return True



def main():
    cant = int(input("Ingrese la cantidad de elementos en la lista: "))
    lista = agregarNumeros(cant)
    print("Primera Lista: ", lista)

    producto = calcularProducto(lista)
    print("El procucto de los elementos en la lista es: ", producto)

    numBorrar = int(input("Elija un numero de la lista a eliminar: "))
    lista = borrarNumero(lista, numBorrar)
    print("Lista despues de los cambios: ", lista)

    if comprobarCapicua(lista) == False:
        print("La lista no es capicúa.")
    else:
        print("La lista es capicúa.")
main()