def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]

    return suma


lista_candidaturas = []
lista_votos = []
lista_porcentajes = []

print('Ve introduciendo candidaturas, o vacío para acabar... ')

candidaturas = ' '
while candidaturas != '':
    candidaturas = input('Nueva candidatura: ')
    if candidaturas != '':
        lista_candidaturas.append(candidaturas)

for c in range(len(lista_candidaturas)):
    votos = int(input('Votos para {}: ' .format(lista_candidaturas[c])))
    lista_votos.append(votos)

total_votos = suma_lista(lista_votos)

for c in range(len(lista_votos)):
    lista_porcentajes.append(lista_votos[c] * 100 / total_votos)

for c in range(len(lista_candidaturas)):
    print('\t{0:.2f}% de los votos a candidaturas para {1}' .format(lista_porcentajes[c], lista_candidaturas[c]))
