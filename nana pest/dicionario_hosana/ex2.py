dicionario = {
    'pc' :40,
    'mouse': 40,
    'ar-condicioado': 2,
    'datashow' : 1
}

print(dicionario['mouse'])

dicionario['mouse'] = 39

print(dicionario)

dicionario['teclado'] = 40

print(dicionario)

#remover elementos
dicionario.pop('mouse')

print(dicionario)