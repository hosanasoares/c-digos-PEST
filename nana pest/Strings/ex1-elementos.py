str = 'maravilhosana'

print(f'primeiro elemento: {str[0]}')
print(f'segundo elemento: {str[1]}')
print(f'terceiro elemento: {str[2]}')
print(f'quarto elemento: {str[3]}')
print(f'quinto elemento: {str[4]}')
print(f'sexto elemento: {str[5]}')

print(f'ultimo elemento: {str[-1]}')
print(f'penultimo elemento: {str[-2]}')

tamanho = len(str)

print('o tamanho é:', tamanho,'caracteres')

print('acessando todos os elementos da string:')

# for i in range(tamanho):
#     print(str[i]) # printa os caracteres
#     print(i) # printa os números dos caracteres

# for n in range(len(str) -1,-1,-1):
#     print(str[n])


# for h in range(-1, - tamanho -1, -1):
#     print(str[h])

print('acessando todos os elementos da string (v2):')

for caractere in str:
    print(caractere)
    