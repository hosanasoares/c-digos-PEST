frase = str(input('digite uma frase: ')).lower()

frase = frase.replace('', '')

dic = {}

for letra in frase:

    if letra in dic:
        dic[letra] += 1

    else:
        dic[letra] = 1

for k, v in dic.items():
    print(f'{k} - {v}')