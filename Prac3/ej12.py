def contar_divisores(n):

    divisores = 0

    for cont in range(1, n + 1):
        if n % cont == 0:
            divisores += 1

    return divisores


def es_primo(n):
    return contar_divisores(n) == 2


def leer_entero_mayor_que(n):

    n2 = int(input('Introduce un entero mayor que {}: ' .format(n)))

    while n2 <= n:
        n2 = int(input('Esperaba entero mayor que {} y {} no lo es. Dame otro: ' .format(n, n2)))

    return n2


num = int(input('Introduce un entero mayor que 0: '))

while num <= 0:
    num = int(input('Esperaba entero mayor que 0 y {} no lo es. Dame otro: '.format(num)))

num2 = leer_entero_mayor_que(num)

print('Voy a buscar primos entre {} y {}...' .format(num, num2))
print('Encontrados: ', end='')

encontrados = False

for contador in range(num, num2 + 1):
    if es_primo(contador):
        print(contador, end=' ')
        encontrados = True

if not encontrados:
    print('ninguno')