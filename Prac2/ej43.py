n = int(input('Introduce un número entero: '))

cantidad_divisores = 0
numero_con_mas_div = 1
divisores_num_con_mas_div = 1

for contador in range(2, n+1):

    for divisor in range(1, contador+1):

        if contador % divisor == 0:
            cantidad_divisores += 1

    if cantidad_divisores >= divisores_num_con_mas_div:
        numero_con_mas_div = contador
        divisores_num_con_mas_div = cantidad_divisores

    cantidad_divisores = 0

print('El número con más divisores es {} ({} divisores)' .format(numero_con_mas_div, divisores_num_con_mas_div))
