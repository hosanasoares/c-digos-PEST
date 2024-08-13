lista = [2, 56, 44, 1000, 456, 89, 10]

num = int(input('digite um número: '))
pos = int(input('digite uma posição: '))

lista.insert(pos, num)

tam = len(lista)

if pos > tam:
    print('não existe essa posição')

print(lista)