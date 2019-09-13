n = int(input('Introduce un número entero: '))

print('Los números primos menores que', n, 'son:', end=' ')

es_primo = True
candidato = 2
contador = 2

while contador < n:                               # Bucle para recorrer los números de 2 hasta n
    while es_primo and candidato < contador:      # Bucle para comprobar si es primo o no
        if contador % candidato == 0:
            es_primo = False
        candidato += 1

    if es_primo:                     # Si es primo lo imprime
        print(contador, end=' ')

    es_primo = True                  # Las variables vuelven a su valor inicial para poder comprobar el número siguiente
    candidato = 2
    contador += 1                    # El contador se incrementa en 1 (pasa al número siguiente que sea menor que n)




