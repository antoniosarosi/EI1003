n = int(input('Introduce un número entero: '))

fibonacci = 1

ultimo_num = 0
anterior = 0

posicion = 1

print('Los {} primeros números de fibonacci son: 1' .format(n), end='')
while posicion < n:
    anterior = ultimo_num
    ultimo_num = fibonacci
    fibonacci = anterior + ultimo_num
    posicion += 1
    print('', fibonacci, end='')
