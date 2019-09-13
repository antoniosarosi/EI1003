def sumar_divisores_propios(n):

    suma_div_propios = 0

    for div in range(1, n):
        if n % div == 0:
            suma_div_propios += div

    return suma_div_propios


def es_abundante(n):
    return sumar_divisores_propios(n) > n


n = int(input('Introduce un número entero: '))

print('Los números abundantes menores que', n, 'son: ', end='')

for cont in range(1, n):
    if es_abundante(cont):
        print(cont, end=' ')
