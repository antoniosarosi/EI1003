a=float(input('Introduce un ángulo (en grados): '))

if a==0:
    print('Nulo')

elif a>0 and a<90:
    print('Agudo')

elif a==90:
    print('Recto')

elif a>90 and a<180:
    print('Obtuso')

elif a==180:
    print('Llano')

elif a>180 and a<360:
    print('Cóncavo')

elif a==360:
    print('Completo')