n=int(input('Introduce un número entero: '))

contador=0

while contador<(n-1):
    contador=contador+1
    print('{}, ' .format(contador), end="")

print(contador+1)