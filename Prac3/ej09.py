def sumar_divisores_propios(n):

    suma_div_propios = 0

    for div in range(1, n):
        if n % div == 0:
            suma_div_propios += div

    return suma_div_propios


def es_abundante(n):
    return sumar_divisores_propios(n) > n


n = int(input('Introduce un número entero: '))
print('Los', n, ' primeros números abundantes son: ', end='')

contador = 2

for cantidad in range(n):

    while es_abundante(contador) is False:
        contador += 1

    print(contador, end=' ')
    contador += 1


