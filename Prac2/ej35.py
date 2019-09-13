n = int(input('Introduce un número entero: '))

factorial = 1
contador = 1

while factorial <= n:
    factorial = factorial * contador
    contador += 1



print('el número buscado es {0} ({1}! <= {2} < {3}!)' .format(contador -1, contador-2, n, contador-1))

