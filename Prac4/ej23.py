from modulomatrices import leerMatrizEnteros


def producto_diagonal_secundaria(matriz):

    if len(matriz) != len(matriz[0]):
        return None

    suma = 1
    for i in range(-1, -len(matriz[0]) - 1, -1):
        suma *= matriz[-i - 1][i]

    return suma


nombreFichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(nombreFichero)

if producto_diagonal_secundaria(matriz) is None:
    print('Error. Se requiere una matriz cuadrada')
else:
    print('El producto de los elementos en la diagonal secundaria es', producto_diagonal_secundaria(matriz))
