def primeiro_e_ultimo(string : str):
    primeiro_caractere = string[0]
    tamanho = len(string)
    ultimo_caractere = string[tamanho-1]
    res = primeiro_caractere + ultimo_caractere
    return res

    # return string[0] + string[-1]



nova_string= str(input('digite uma palavra: '))

print(primeiro_e_ultimo(nova_string))