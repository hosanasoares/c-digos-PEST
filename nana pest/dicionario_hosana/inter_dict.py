#como interar dicionarios

dicionario = {
    'computador': 40, 
    'mouse': 39,
     'mesa': 20,
     'datashow': 1,
     'ar-condicionado': 2
}

# como interar pelas chaves
for item in dicionario.keys():
    print(item)

# como interar pelos valores
for item in dicionario.values():
    print(item)

#como interar pelas chaves e valores (k, v)

for k, v in dicionario.items():
    print(k)
    print(v)
    print(f'chave = {k}, valor = {v}')