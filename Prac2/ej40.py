n = int(input('Introduce un número entero: '))

print('Los', n, 'primeros números primos son:', end=' ')

es_primo = True
candidato = 2
contador = 2
cantidad = 1

while cantidad <= n:                              # Bucle para imprimir los n primos pedidos
    while es_primo and candidato < contador:      # Bucle para comprobar si es primo o no
        if contador % candidato == 0:
            es_primo = False
        candidato += 1

    if es_primo:                     # Si es primo lo imprime
        print(contador, end=' ')
        cantidad += 1                # Como el numero es primo, la cantidad se incrementa en 1, hasta llegar a n

    es_primo = True                  # Las variables vuelven a su valor inicial para poder comprobar el número siguiente
    candidato = 2
    contador += 1                    # El contador se incrementa en 1
