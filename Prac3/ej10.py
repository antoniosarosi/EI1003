def sumar_divisores_propios(n):

    suma_div_propios = 0

    for div in range(1, n):
        if n % div == 0:
            suma_div_propios += div

    return suma_div_propios


def son_amigos(a, b):
    return a == sumar_divisores_propios(b) and b == sumar_divisores_propios(a)


seguir = 'S'

while seguir == 'S':
    a = int(input('Introduce un número entero a: '))
    b = int(input('Introduce un número entero b: '))

    print('Los dos números son amigos') if son_amigos(a, b) else print('Los dos números no son amigos')
    seguir = input('¿Seguimos comprobando amistades (S/N)? ')

print('¡Adiós!')
