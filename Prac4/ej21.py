from modulomatrices import leerMatrizEnteros


def sumar_columna(matriz, columna):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][columna]

    return suma


nombreFichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(nombreFichero)

for c in range(len(matriz[0])):
    print('La suma de los elementos en la columna {} es {}' .format(c, sumar_columna(matriz, c)))
