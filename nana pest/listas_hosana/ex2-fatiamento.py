#fatiamento
l= ['a', 1, 'b', 2, 'c', 3, 'd', 4]
print(l[::2])
print(l[1::2])

#dada a lista: l = ['0', 'python', 'é', 'uma', 'linguagem', 'massa']
#crie uma nova lista contendo apenas os elementos "python', 'é", 'uma', usando fatiamento
l = ['0', 'python', 'é', 'uma', 'linguagem', 'massa']
l1 = l[1:4:]
print(l1)

#percorrendo uma lista
l= ['a', 1, 'b', 2, 'c', 3, 'd', 4]
tam_da_lista = len(l)

for i in range(tam_da_lista):
    print(l[i])

for elemento in l:
    print(l)

