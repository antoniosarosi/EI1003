importe=float(input('Introduce el importe de la compra: '))
zona=input('Introduce la zona de envío (A/B/C): ')
socio=input('¿Eres socio (S/N)? ')

if importe<=150 and socio=='N':
    gastos=25
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

elif importe<=150 and socio=='S':
    gastos=19
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

elif importe>150 and importe<=750 and socio=='N':
    gastos=60
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

elif importe>150 and importe<=750 and socio=='S':
    gastos=49
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

elif importe>750 and importe<=1500 and socio=='N':
    gastos=120
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

elif importe>750 and importe<=1500 and socio=='S':
    gastos=89
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

elif importe>1500 and socio=='N':
    gastos=importe*8/100
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

else:
    gastos=importe*6/100
    if zona=='B':
        gastos=gastos+30
    elif zona=='C':
        gastos=gastos+69
    else:
        gastos=gastos

print('Gastos de envío: {0:.2f} euros' .format(gastos))







