n=int(input('Introduce un número entero: '))

contador=2

if n%2==0:
    while contador<=n:
        print(contador)
        contador=contador+2

else:
    while contador<n:
        print(contador)
        contador = contador + 2

