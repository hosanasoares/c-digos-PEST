dic = {}
soma = 0
for i in range(3):
    chave = str(input('digite um nome: '))
    valor = int(input(f'digite a idade de {chave}: '))
    dic[chave] = [valor]
    soma += valor

tam = len(dic)
med = soma/tam

print(f'a média das idades é {med}')