a = input('Introduce una cadena de caracteres A: ')
b = input('Introduce una cadena de caracteres B: ')

es_sufijo = True

if len(b) <= len(a):
    for r in range(-1, -len(b) - 1, -1):
        if b[r] != a[r]:
            print('B no es sufijo de A')
            es_sufijo = False
            break

    if es_sufijo:
        print('B es sufijo de A')

else:
    print('B no es sufijo de A')