def contar_divisores(n):

    divisores = 0

    for cont in range(1, n + 1):
        if n % cont == 0:
            divisores += 1

    return divisores


def es_primo(n):
    return contar_divisores(n) == 2


a = int(input('Introduce un entero estrictamente positivo: '))
b = int(input('Introduce un entero mayor que {}: ' .format(a)))
print('Voy a buscar primos entre {} y {}...' .format(a, b))
print('Encontrados: ', end='')

encontrados = False              # Suponemos que no encontrará primos para imprimir 'Ninguno' sin problemas

for contador in range(a, b + 1):
    if es_primo(contador):
        print(contador, end=' ')
        encontrados = True

if not encontrados:
    print('ninguno')
