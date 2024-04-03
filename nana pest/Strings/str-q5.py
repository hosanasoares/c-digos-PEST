def concatenar_fatiar(string1 : str, string2 : str):
    str1 = string1[:3]
    str2 = string2[-3::-3]

    soma = str1 + str2

    return soma


str1 = str(input('digite a primeira palavra : '))
str2 = str(input('digite a segunda palavra :'))

print(concatenar_fatiar(str1, str2))