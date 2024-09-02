# como criar um dicionário 

strings = ''
listas = []
tuplas = ()
dicionario = {}

dicionario = dict()

en_ptbr = {
    "one" : "um",
    "two" : "dois",
    "three": "três"} #chave/ valor

print(en_ptbr)
# 2 como acessar os valores do dicionário

print(en_ptbr['one'])
print(en_ptbr['two'])
print(en_ptbr['three'])

lista = [1,2,3]
lista[0]= 0
lista[1]= 0
lista[2]= 0

print(lista)

lista.append('x')

#qadiconar e substituir é o mesmo metodo
en_ptbr['four'] = 'quatro'

print(en_ptbr)

dic = {}
for n in range(4):
    chave = str(input('digite o valor de uma chave: '))
    valor = str(input('digite um valor para a chave : '))
    dic[chave] = valor

chave= input('qual chave você quer pesquisar: ')

print(dic[chave])

if chave in dic:
    print(dic[chave])

else:
    print('inexistente')

#verficar se a chave existe no dicionario
if 'two' in en_ptbr:
    print('a chave existe')

else:
    print('a chave não existe')

#como remover um intem de um dicionario

del en_ptbr['one']

en_ptbr.pop('two')

#como limpar dicionario

en_ptbr.clear()

#como copiar um dicionario
outro_dic = en_ptbr.copy()