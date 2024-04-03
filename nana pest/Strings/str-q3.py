def reverter(string : str):
    
    fatiamento = string[-1::-1]

    return fatiamento


string = str(input('digite uma palavra: '))

print(reverter(string))