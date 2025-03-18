#Escriba una funcion que reciba como parámetros un número de dia, un numero de mes y un numero de año y devuelva la cantidad de dias que faltan hasta fin de mes.
#Luego desarrollar tres programas para:
#Ingresar una fecha formada por tres enteros (dia, mes y año) e imprimir la cantidad de dias que faltan hasta fin de año
#Ingresar una fecha formada por tres enteros e imprimir la cantidad de dias transcurridos en ese año hasta esa fecha
#Ingresar dos fechas formadas por tres enteros e iomprimir cuanto tiempo transcurrio entre ambas, expresando el resultado en años, meses, dias

dias30 = [4, 6, 9, 11]
dias31 = [1, 3, 5, 7, 8, 10, 12]

def compararFechas(dd, mm, yyyy):
    fecha1 = dd, mm, yyyy
    fecha2 = main()

def diasHastaFecha(dd, mm, yyyy):
    contd = dd
    mes = 1
    for mes in range(1, mm):
        if mes in dias30:
            contd += 30
        elif mes in dias31:
            contd += 31
        else:
            contd += 29 if esBisiesto(yyyy) == True else 28
    return contd

def calcularFinDeAño(fdm, mm, yyyy):
    contd = fdm
    mes = mm
    for mes in range(mm + 1, 13):
        if mes in dias30:
            contd += 30
        elif mes in dias31:
            contd += 31
        else:
            contd += 29 if esBisiesto(yyyy) == True else 28
    return contd

def calcularFinDeMes(dd, dias):
    resultado = dias - dd
    return resultado

def esBisiesto(yyyy):
    if (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0):
        return True
    else: 
        return False

def main():
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
        dias = 30
    elif mm in dias31:
        dias = 31
    else:
        if esBis == True:
            dias = 29
        else:
            dias = 28
    
    dd = int(input("Ingrese el número del día: "))
    while dd < 1 or dd > dias:
        print("Ingrese una día válido.")
        dd = int(input("Ingrese el número del día: "))


    print(f"La fecha seleccionada es: {dd}/{mm}/{yyyy}")

    fdm = calcularFinDeMes(dd, dias)
    print(f"Faltan {fdm} días para que termine el mes.")

    fda = calcularFinDeAño(fdm, mm, yyyy)
    print(f"Faltan {fda} días para que termine el año")

    dhf = diasHastaFecha(dd, mm, yyyy)
    print(f"Transcurrieron {dhf} hasta la fecha introducida.")
    
    

main()