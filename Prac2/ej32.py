n = int(input('Introduce un número entero: '))

factorial = 1

for contador in range(1, n + 1):
    print('{}! = {}' .format(contador, contador * factorial))
    factorial *= contador
