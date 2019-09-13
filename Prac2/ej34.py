'''
versión eficiente :

        num = int(input('Introduce un número entero: '))
        resultado = 1

        for i in range(1, num +1):
            resultado *= i
            if resultado == num:
                break
        print('{} es el factorial de {}' .format(num, i))
'''

# Versión cutre :

n = int(input('Introduce un número entero: '))

contador = 1
stop = 1
factorial = 1

if n == 1:
    print('1 es el factorial de 1')

else:
    while stop <= n:
        factorial = contador * factorial

        if factorial == n and contador>2:
            stop = n
            contador = contador-1

        elif factorial == n and contador == 2:
            stop = n
            contador = contador-1

        else:
            contador = contador + 1
            stop = stop + 1

    print('{} es el factorial de {}' .format(n, contador))


