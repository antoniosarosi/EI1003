from modulomatrices import leerMatrizEnteros


def sumar_elementos(matriz):
    suma = 0
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            suma += matriz[i][k]

    return suma


nombreFichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(nombreFichero)
print('La suma de todos los elementos en la matriz es', sumar_elementos(matriz))
