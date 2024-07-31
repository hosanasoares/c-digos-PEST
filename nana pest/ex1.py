1# exemplos de lista

l = ['a','bom', 100, 5.5, '']
print(type)

# lista vazia

l1 = []
l2= list()

print(l[0])
print(l[3])
#print(l[5]) #erro

#modificando elementos 
l[0] = 'x'
print(l)

str1 = 'ovo'
str2 = 'ana'
str3 = str1
print(str3)#ovo

str1 = 'ana'
str2 = 'ovo'
print(str3) #ovo

l1 = ['o', 'v', 'o']
l2 = ['a', 'n', 'a']
l3 = l1
print(l3)

l2 = ['o', 'v', 'o']
l1 = ['a', 'n', 'a']
print(l3)

#copiando listas
l1 = [1, 2, 3]
l2 = [4, 5, 6]
lc = l1
print(lc)

print(f'l1 : {l1}')
print(f'lc: {lc}')

l1 = [0]
print(lc)


print(f'l1 : {l1}')
print(f'lc: {lc}')

#armazenar notas: média aritmética
notas = [10, 7.5, 3.6, 8.1, 5]
soma = 0 

for nota in notas:
    soma += nota

media = soma / len(notas)
print(media)

# leia 5 notas do usuário, coloque-as em uma lista, e calcule a média dessas notas.
#obs: só calcule a média depois que as notas estiverem na lista

lista = []
for nota in range(5):
    nota = float(input('digite uma nota: '))
    lista = [nota]
    soma += nota

media = soma/ len(lista)
print('a média é:' , media)

copia = l1[:]
l1[0] = 'x'
copia[0] = 'y'

