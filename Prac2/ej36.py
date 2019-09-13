n = int(input('Introduce un número entero: '))

fibonacci = 1       # Esta variable será la sucesión de Fibonacci, que en este ejercicio empieza en 1

ultimo_num = 0      # Estas dos variables serán la suma de un número de la sucesión más el anterior
anterior = 0

posicion = 1        # variable para sacar la posición dentro de la sucesión

while posicion < n:
    anterior = ultimo_num
    ultimo_num = fibonacci
    fibonacci = anterior + ultimo_num
    posicion += 1

print('Fibonacci({}) = {}' .format(posicion, fibonacci))
