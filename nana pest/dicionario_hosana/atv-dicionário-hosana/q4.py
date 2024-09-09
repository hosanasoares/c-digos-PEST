dic = {}

for i in range(3):
    chave = str(input('digite um nome: '))
    valor = int(input(f'digite a idade de {chave}: '))
    dic[chave] = [valor]

for k, v in dic.items():
    print(f'{k}:{v}')