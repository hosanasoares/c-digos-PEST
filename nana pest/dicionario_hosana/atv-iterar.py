def mostrar_dicionario(dict):
    for k, v in dic.items():
        print(f'[{k}] : [{v}]')


dic = {}
for n in range(3):
    chave = str(input('digite o valor de uma chave: '))
    valor = str(input('digite um valor para a chave : '))
    dic[chave] = valor


perg = str(input('digite uma chave que você queira acessar: '))
print(dic[perg])
