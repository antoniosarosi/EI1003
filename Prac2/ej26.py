numero=int(input("Introduce un número entero: "))

contador=1
divisible=0

while contador <= numero:
    if numero%contador == 0:
        divisible=divisible+1
        contador=contador+1
    else:
        contador=contador+1

print('Es primo') if divisible == 2 else print('No es primo')

'''

Versión eficiente : 

n = int(input('Dame un número entero : '))

es_primo = True
candidato = 2

while es_primo and candidato < n:       #  Una variable puesta sola significa variable == True
    if n % candidato == 0:
        print('Encontrado un divisor: {}' ,format(n))
        es_primo = False
    candidato += 1

print('El numero {} es primo' .format(n)) if es_primo else print('El numero {} no es primo' .format(n))

'''