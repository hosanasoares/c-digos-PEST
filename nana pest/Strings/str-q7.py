def intervendo_substrings(str1 : str, str2: str):
        str1 = str1[::-1]
        str2 = str2[::-1]

        tam1 = len(str1)
        tam2 = len(str2)

        
        metade1 = str2[:tam2//2]

        metade2 = str1[tam1//2:]


        soma =  metade1 + metade2
        return soma


str1 = str(input('digite uma palavra: '))
str2 = str(input('digite outra palavra: '))

print(intervendo_substrings(str1, str2))


