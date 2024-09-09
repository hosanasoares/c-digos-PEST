dic = {}
for n in range(3):
    chave = str(input('digite uma matéria: '))
    valor = int(input(f'digite a nota da matéria de {chave}: '))
    dic[chave] = [valor]

for k, v in dic.items():
    print(f'{k}:{v}')