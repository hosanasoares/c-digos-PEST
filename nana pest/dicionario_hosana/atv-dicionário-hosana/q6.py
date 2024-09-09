dic = {}
soma = 0
for i in range(5):
    chave = str(input('digite um nome: '))
    valor = int(input(f'digite a idade de {chave}: '))
    dic[chave] = [valor]
    soma += valor

tam = len(dic)
for n in range(tam):
    med = soma/tam
    
print(f'a média da pontuação dos jogadores é: {med}')