n = int(input('Introduce un número entero: '))

print('los', n, 'primeros números abundantes son:', end=" ")

cantidad = 0                                                 # En principio la cantidad de abundantes es 0 (tiene que llegar a n)

abundantes = 2                                               # Esta variable servirá para comprobar si los números son abundantes

while cantidad < n:

    contador = 2                                             # Aquí reiniciamos los valores necesarios para comprobar el número siguiente
    es_abuntante = False
    suma_divisores_propios = 0

    while not es_abuntante and contador < abundantes:

        if abundantes % contador == 0:                       # Cada vez que el resto es 0 la suma se incrementa con el divisor correspondiente
            suma_divisores_propios += contador

        contador += 1                                        # Incremento del contador

        if suma_divisores_propios > abundantes:              # Si es abundante lo imprimimos y paramos el bucle
            es_abuntante = True
            print(abundantes, end=' ')
            cantidad += 1                                    # Cuando cantidad llegue a n se para el bucle principal

    abundantes += 1                                          # Pasamos al número siguiente
