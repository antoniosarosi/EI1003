def mostrar_cadena_repetida(c, n, s):

    for cont in range(n-1):
        print(c + s, end='')
    print(c)


cadena = input('Introduce una cadena: ')
separador = input('Introduce un separador: ')
m = int(input('Introduce un máximo de repeticiones: '))

for i in range(1, m + 1):
    mostrar_cadena_repetida(cadena, i, separador)
