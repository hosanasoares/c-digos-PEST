frase = str(input('digite uma frase: ')).lower()
pont = ','

for p in pont:
    frase = frase.replace(p , '')

separa = frase.split()

dic = {}

for palavra in separa:
    if palavra in dic:
        dic[palavra] += 1

    else:
        dic[palavra] = 1

for k, v in dic.items():
    print(f'{k} - {v}')