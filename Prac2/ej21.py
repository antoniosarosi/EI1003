n=int(input('Introduce un número entero: '))
contador=1

while (contador**2)<n:
    print('El cuadrado de {} es {}' .format(contador, contador**2))
    contador=contador+1