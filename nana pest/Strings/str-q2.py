def intervalo(string : str, indice1 : int, indice2 : int):
    fatiamento = string[indice1 : indice2]

    return fatiamento

print('='*30)
string = str(input('digite uma palavra: '))
print('='*30)
ind1 = int(input('digite o primeiro número do intervlo : '))
print('='*50)
ind2 = int(input('digite o segundo número do intervalo: '))
print('='*50)

print(intervalo(string, ind1, ind2))