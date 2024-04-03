def saltos(string : str, num : int):
    
    pulo = string[:: num]

    return pulo



string = str(input('digite uma palavra: '))
pulo = int(input('digite o número de saltos: '))

print(saltos(string, pulo))