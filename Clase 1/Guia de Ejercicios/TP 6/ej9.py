#Escriba una funcion que reciba como parámetros un número de dia, un numero de mes y un numero de año y devuelva la cantidad de dias que faltan hasta fin de mes.
#Luego desarrollar tres programas para:
#Ingresar una fecha formada por tres enteros (dia, mes y año) e imprimir la cantidad de dias que faltan hasta fin de año
#Ingresar una fecha formada por tres enteros e imprimir la cantidad de dias transcurridos en ese año hasta esa fecha
#Ingresar dos fechas formadas por tres enteros e iomprimir cuanto tiempo transcurrio entre ambas, expresando el resultado en años, meses, dias

dias30 = [4, 6, 9, 11]
dias31 = [1, 3, 5, 7, 8, 10, 12]

def esBisiesto(yyyy):
    if (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0):
        return True
    else: 
        return False

def ingresarFecha():
    yyyy = int(input("Ingrese el número del año: "))
    while yyyy <= 0:
        print("Ingrese un año válido.")
        yyyy = int(input("Ingrese el número del año: "))

    esBis = esBisiesto(yyyy)

    mm = int(input("Ingrese el número del mes: "))
    while mm < 1 or mm >12:
        print("Ingrese un més valido")
        mm = int(input("Ingrese el número del mes: "))
    if mm in dias30:
        aux = 30
    elif mm in dias31:
        aux = 31
    else:
        if esBis == True:
            aux = 29
        else:
            aux = 28
    
    dd = int(input("Ingrese el número del día: "))
    while dd < 1 or dd > aux:
        print("Ingrese una día válido.")
        dd = int(input("Ingrese el número del día: "))
    
    fecha = f"{dd}/{mm}/{yyyy}"
    print(fecha)

ingresarFecha()