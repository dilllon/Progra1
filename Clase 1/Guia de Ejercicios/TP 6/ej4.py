#Devolver True si el número entero recibido como primer parámetro es múltiplo del segundo, o False en caso contrario.
#Ejemplo: esMultiplo(40, 8) devuelve true, y esMultiplo(50, 3) devuelve False

def esMultiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


def main():
    num1 = int(input("Ingrese el primer parámetro: "))
    num2 = int(input("Ingrese el segundo parámetro: "))
    
    if esMultiplo(num1, num2) == True:
        print(num1, " es múltiplo de ", num2)
    else:
        print(num1, " no es múltiplo de ", num2)

main()