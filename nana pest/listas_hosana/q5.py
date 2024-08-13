lista = ['fortaleza', 'são paulo', 'joão pessoa', 'paris', 'lisboa', 'aveiro']

nome = str(input('digite o nome de uma cidade: '))


if nome in lista:
    print('essa cidade existe na lista. ')

else:
    print('essa cidade não existe na lista. ')

print(lista)