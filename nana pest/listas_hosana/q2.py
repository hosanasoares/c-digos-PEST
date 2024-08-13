lista = ['banana', 'morango', 'jabuticaba', 'tangerina', 'uva', 'maçã']

fruta = str(input('digite o nome de uma fruta: '))

if fruta in lista:
        lista.remove(fruta)
else:
    print('não existe')  

print(lista)

