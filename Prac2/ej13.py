veces=int(input('¿Cuántas veces prevés utilizar el gimnasio? '))

tarjeta=50

num_bonos=veces//10
num_entradas=veces % 10

if num_entradas==0:
    bonos=num_bonos
else:
    bonos=num_bonos+1

precio_solo_bonos=bonos*20

precio_bonos_y_entrads=num_bonos*20+num_entradas*3

minimo=tarjeta
if precio_solo_bonos<minimo:
    minimo=precio_solo_bonos
if precio_bonos_y_entrads<minimo:
    minimo=precio_bonos_y_entrads

if minimo==tarjeta:
    recomendacion='tarjeta.'
elif minimo==precio_solo_bonos:
    recomendacion='bonos.'
else:
    recomendacion='bonos y entradas.'

print('Con tarjeta: {0} euros.\nCon bonos ({1}): {2} euros.\nCon bonos ({3}) y entradas ({4}): {5} euros.\nRecomendación: {6} ' .format(tarjeta, bonos, precio_solo_bonos, num_bonos, num_entradas, precio_bonos_y_entrads, recomendacion ))

