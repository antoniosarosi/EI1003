n = int(input('Introduce un número entero: '))

suma_divisores_propios = 0

print('los números abundantes menores que', n, 'son:', end=' ')

for i in range(2, n):                                     # Bucle para recorrer los números de 2 a n

    for contador in range(2, i):                          # Bucle para comprobar si es o no abundante
        if i % contador == 0:
            suma_divisores_propios += contador

    if suma_divisores_propios > i:                        # Si es abundante lo imprime
        print(i, end=' ')

    suma_divisores_propios = 0                            # Reinicia el valor de la suma para comprobar el siguiente número