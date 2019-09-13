n=int(input('Introduce un número entero: '))

contador = 1
suma = 0

while contador <= n:
    if contador % 3 == 0 or contador % 5 == 0:
        contador=contador+1
    else:
        suma=suma+contador
        contador=contador+1

print('La suma es', suma)