from modulomatrices import leerMatrizEnteros


def sumar_fila(matriz, fila):
    suma = 0
    for i in range(len(matriz[fila])):
        suma += matriz[fila][i]

    return suma


nombreFichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(nombreFichero)

for f in range(len(matriz)):
    print('La suma de los elementos en la fila {} es {}' .format(f, sumar_fila(matriz, f)))
