from modulomatrices import leerMatrizEnteros


def sumar_diagonal(matriz):

    if len(matriz) != len(matriz[0]):
        return None

    suma = 0
    for i in range(len(matriz[0])):
        suma += matriz[i][i]

    return suma


nombreFichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(nombreFichero)

if sumar_diagonal(matriz) is None:
    print('Error. Se requiere una matriz cuadrada')
else:
    print('La suma de los elementos en la diagonal principal es', sumar_diagonal(matriz))