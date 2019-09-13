n=int(input("Introduce un número entero: "))

contador=1
divisores=0

while contador <= n:
    if n%contador==0:
        divisores=divisores + contador
        contador = contador +1
    else:
        contador=contador+1

print('La suma de los divisores de {} es {}' .format(n, divisores))