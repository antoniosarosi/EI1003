n=int(input("Introduce un número entero: "))

contador=1
divisores=0

while contador <= n:
    if n%contador==0:
        divisores=divisores + 1
        contador = contador +1
    else:
        contador=contador+1

print('El número {} tiene {} divisores' .format(n, divisores))