from modulomatrices import leerMatrizEnteros


def sumar_encima_diagonal(matriz):

    if len(matriz) != len(matriz[0]):
        return None

    suma = 0
    for i in range(len(matriz[0]) - 1):
        for k in range(i + 1, len(matriz[0])):
            suma += matriz[i][k]

    return suma


nombreFichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(nombreFichero)

if sumar_encima_diagonal(matriz) is None:
    print('Error. Se requiere una matriz cuadrada')
else:
    print('La suma de los elementos por encima de la diagonal principal es', sumar_encima_diagonal(matriz))
