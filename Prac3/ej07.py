def contar_divisores(n):

    divisores = 0

    for cont in range(1, n + 1):
        if n % cont == 0:
            divisores += 1

    return divisores

n = int(input("Introduce un número entero: "))
num_con_mas_div = 1
max_divisores = 1

for contador in range(1, n + 1):
    if contar_divisores(contador) >= max_divisores:
        num_con_mas_div = contador
        max_divisores = contar_divisores(contador)

print('El número con más divisores es {} ({} divisores)' .format(num_con_mas_div, max_divisores))