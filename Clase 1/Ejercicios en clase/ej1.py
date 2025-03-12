lista = []
listab = []
suma = 0
promedio = 0

numEl = int(input("Ingrese la cantidad de elementos de la lista: "))

for i in range(numEl):
    lista.append(int(input("Ingrese un número: ")))
    suma += lista[i]
    promedio = suma / numEl

print("La lista es: ", lista)
print("Promedio: ", promedio)

for i in range(lista[i]):
    if lista[i] > promedio:
        listab.append(lista[i])

print("Los números mayores al promedio son: ", listab)