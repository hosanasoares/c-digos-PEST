#operações entre strings

#1. concatenação
str1 = 'bom'
str2 = ' '
str3 = 'dia'
res = str1 + str2 +str3
print(res)

#2. repetição ('multiplicação') de strings

str1 = 'nana'
res = 4 * str1 + 'ba'
print(res)


nome = str(input('digite uma frase ou palavra: '))

res = "*" + nome[1:]

print(res)