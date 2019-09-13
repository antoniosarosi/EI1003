n = int(input('Introduce un número entero: '))

factorial = 1

for n in range(1, n + 1):
    factorial = factorial * n
    print('{}! = {}' .format(n, factorial))




