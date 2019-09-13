from math import sqrt

a=float(input('Introduce a: '))
b=float(input('Introduce b: '))
c=float(input('Introduce c: '))

print('x1 = ', (-b+sqrt(b**2-4*a*c))/(2*a))
print('x2 = ', (-b-sqrt(b**2-4*a*c))/(2*a))