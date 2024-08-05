#maior número da lista

lista = [1, 344, -15, 1989, 2007, 23.5, 12, 25, 67.3]

maior_numero = -99999

for item in lista:
    if item > maior_numero:
        maior_numero = item

print(maior_numero)