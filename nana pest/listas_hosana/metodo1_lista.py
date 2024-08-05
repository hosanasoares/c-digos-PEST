#adicionar elementos na lista - APPEND(fim da lista)

l = [3, 5, 67, 10, 8, 5000]

tamanho_da_lista= len(l)
print(l)

print('tamanho da lista antes do append: ', tamanho_da_lista)
l.append('garrafa')

tamanho_da_lista= len(l)

print('tamanho da lista depois do append:', tamanho_da_lista)
print(l)


#função recebe lista e elemento sozinho. Adicionar o elemento no final da lista e retornar a lista nova.

def adc_lista(lista : list, elemento ):
    minha_lista.append(elemento)
    return minha_lista


minha_lista = [1, 2, 3, 4]

print(adc_lista(minha_lista, 'A'))

#adicionar elementos na lista - INSERT

l = [3, 5, 67, 10, 8, 5000]
tamanho = len(l)

print(l)
print('tamanho antes: ', tamanho)

l.insert(2, 'a')

tamanho = len(l)

print(l)
print('tamanho depois:', tamanho)

l.insert(len(l), 'z')

print(l)

#remover elementos da lista - REMOVE
l = [3, 5, 67, 10, 8, 5000]

print(l)
l.remove(10)
print(l)


#função recebe lista e um elemento. Caso o elemento exista na lista, remova-o. Caso não exita, adicione ao final da lista. Sua função não deve retornar nada.

def adc_lista(lista : list, elemento):
    if elemento in lista:
        lista.remove(elemento)

    else:
        lista.append(elemento)

lista = list()
adc_lista(lista, input('digite alguma coisa: '))
print(lista)

adc_lista(lista, input('digite alguma coisa: '))
print(lista)

adc_lista(lista, input('digite alguma coisa: '))
print(lista)

adc_lista(lista, input('digite alguma coisa: '))
print(lista)

adc_lista(lista, input('digite alguma coisa: '))
print(lista)

#removendo elementos da lista - DEL
l = [3, 5, 67, 10, 8, 5000]

print(f'antes: {l}')
del l[5]
print(f"depois: {l}")
