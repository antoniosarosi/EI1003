def calcular_cadena_repetida(c, n, s):

    cadena = ''

    for cont in range(n - 1):
        cadena += c + s
    cadena += c

    return cadena


# Variables globales del programa principal, cadena no equivale a la variable cadena de la función

cadena = input('Introduce una cadena: ')
separador = input('Introduce un separador: ')
m = int(input('Introduce un máximo de repeticiones: '))

for i in range(1, m + 1):
    print(calcular_cadena_repetida(cadena, i, separador))