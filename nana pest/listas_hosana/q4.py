lista = [20, -9, 18, 345, 26, 900, 40, 2]

for n in lista[:]:
    if n % 2 == 0:
        lista.remove(n)

print(lista)