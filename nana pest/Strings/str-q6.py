def letras_alteradas(string : str):
    
    tamanho = len(string)

    for n in range(tamanho):
        
        if n % 2 == 0:
            print(string[n])

        

string = str(input('digite uma palavra: '))


letras_alteradas(string)