n = int(input('Introduce un número entero: '))

suposicion = False

fibonacci = 1

ultimo_num = 0
anterior = 0

posicion = 1        

while posicion <= n:
    anterior = ultimo_num
    ultimo_num = fibonacci
    fibonacci = anterior + ultimo_num

    if fibonacci == n:
        posicion += 1
        print('El número buscado es {}' .format(posicion))
        suposicion = True
        break
    else:
        posicion += 1

if not suposicion:
    print('No es un número de Fibonacci')
