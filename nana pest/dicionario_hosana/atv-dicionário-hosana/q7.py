lista = []
dic = {}
for n in range(3):
    chave = str(input('digite uma palavra: '))
    lista.append(chave)
    tam = len(chave)
    dic[chave] = [tam]

print('a lista de palavras é: ', lista)
print('a lista com os valores da palavra é: ', dic)