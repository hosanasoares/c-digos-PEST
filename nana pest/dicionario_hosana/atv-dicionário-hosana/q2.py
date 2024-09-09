dic = {}

for n in range(4):
    chave = str(input('digite o nome do produto que deseja adiconar: '))
    valor = int(input(f'digite a quantidade do produto {chave} que deseja adiconar: '))
    dic[chave] = [valor]

for k, v in dic.items():
    print(f'{k}:{v}')