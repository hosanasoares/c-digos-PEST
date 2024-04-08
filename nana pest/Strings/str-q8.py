def intercalar_letras(str1 : str, str2 : str):
    tamanho1 = len(str1)
    tamanho2= len(str2)
    nv_str = ''



    if tamanho2 >= tamanho1:
        menor = tamanho1
        maior = tamanho2

        for h in range(menor):
            nv_str += str1[h] + str2[h]

    if not tamanho2 == tamanho1:
        for i in range(h + 1, maior):
            nv_str +=  str2[i]

       

    else:
        menor = tamanho2
        maior = tamanho1

        for n in range(menor):
            nv_str = str1[n] + str2[n]

        for a in range(n +1, maior):
            nv_str += str1[a]
    

    return nv_str


str1 = str(input('digite a primeira palavra: '))
str2 = str(input('digite a segunda palavra: '))

print(intercalar_letras(str1, str2))

