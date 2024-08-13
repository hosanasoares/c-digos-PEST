lista = []

copia = lista[:]

tam = len(lista)

for n in range(tam):
    for i in range(tam):
        if lista[n]> copia[i]:
            copia.remove(lista[n])
            copia.insert(n, lista[n])

print(copia)