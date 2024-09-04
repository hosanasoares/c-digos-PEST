notas = {
    'joao vitor': [9.5, 7.5, 6.1],
    'roberto': [6.3, 8.1, 9.2],
    'fernando': [7.8, 8.1,4]
}

print(notas['roberto'])

for notas in notas['roberto']:
    print(notas)

notas['roberto'].append(10)

print(notas)

