n = int(input('Introduce un número entero: '))

numero_inicial = n

factorial = 1

while n > 1:
    factorial = n * factorial
    n = n - 1

print('{}! = {}' .format(numero_inicial, factorial))

