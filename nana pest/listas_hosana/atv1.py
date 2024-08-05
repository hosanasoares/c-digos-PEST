#lista de frutas
lista = ['laranja', 'maçã', 'morango', 'jabuticaba', 'mamão' ]

fruta = input('digite uma fruta: ')

if fruta in lista:
    print('Essa fruta está na lista.')

else:
    print(f'{fruta} não está na lista.')
