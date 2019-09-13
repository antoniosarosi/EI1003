def contar_divisores(n):
    divisores = 0
    for cont in range(1, n + 1):
        if n % cont == 0:
            divisores += 1
    return divisores


n = int(input("Introduce un número entero: "))
print('El número {} tiene {} divisores' .format(n, contar_divisores(n)))