consumo = float(input('Introduce la cantidad de kWh: '))

if consumo<=100:
    precio=consumo*5

elif consumo>100 and consumo<=250:
    precio=(consumo-100)*7+100*5

else:
    precio=(consumo-250)*10+150*7+100*5

print('importe: {0:.2f} euros' .format(precio/100))
