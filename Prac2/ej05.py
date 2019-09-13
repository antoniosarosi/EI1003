a=float(input('Introduce el lado a: '))
b=float(input('Introduce el lado b: '))
c=float(input('Introduce el lado c: '))

if a==b and a==c:
    print('No es escaleno')

elif a==b or a==c or b==c:
    print('No es escaleno')

else:
    print('Es escaleno')