# métodos de strings
# -------------------
# metodos = funções 

#     com/ sem retorno
#     com/ sem parametros

# 1° capitalaize() - retorna a string com o primeiro caractere em caixa alta

def funcao(palavra : str ): # quando tem o tipo de variavel, e coloca o ponto na variavel, pode ver os metodos da string ou variavel
    palavra.capitalize()  # capitalize é uma função que  retorna  a palavra com a primeira letra maiuscula
    print(palavra.capitalize())
    


funcao('abacaxi')

#2° lower() - converte as strings para minusculo
nome = str(input('digite um nome: '))
print(nome)
print(nome.lower())


#3° upper() -  deixa as strings maiusculas
nome = str(input('digite um nome: '))
print(nome)
print(nome.upper())


#4° split() - divide a string com base em um separador e retorna uma lista

frase = 'hoje eu quero um ciclopentanoperidrofenantreno'
lista_frase = frase.split()
print(lista_frase) # ['hoje', 'eu, 'quero', 'um', 'ciclopentanoperidrofenantreno']
lista_frase = frase.split('x') #separa pela letra dentro dela. se não há a letra que você colocou, então ele se tornará um elemento só dentro da lista
print(lista_frase) #['hoje eu quero um ciclopentanoperidrofenantreno']


#5° join() - une elementos de uma lista, usando uma string como um 'seprador'
frase = 'hoje eu quero um ciclopentanoperidrofenantreno'
lista_frase = frase.split('m')
print(lista_frase)

palavra = '<3'

print(palavra.join(lista_frase))

#6° replace() - substitui um determinado trecho da string por outro
nome = input('digite o seu nome: ').upper()

new_name = nome.replace('a', '*') # onde tiver tal letra, ela será substituida por outra coisa
new_name = new_name.replace('A', '*')
new_name = new_name.replace('S', '*')

print(new_name)


#7° find() -  retorna o indice da primeira ocorrência de um determinado valor
frase = 'hoje é um bom dia'
print(frase.find('m')) #fala em qual posição o inice aparece primeiro
frase = frase.replace('m', 'x')
print(frase.find('m'))

#8° index() - é a mesma coisa do find(), mas dá erro se não existir.
frase = 'hoje é um bom dia'
print(frase.index('m')) 
print(frase.index('a'))

#9° count() -  conta o número de ocorrências, de uma determinada string

frase = 'eu sou mais eu'
print(frase.count('e'))
print(frase.isupper()) # eu quero saber se a string é maiuscula , se não for ele printa falso. se for, ele retorna true 


#10° islower() - retorna true se a string for minuscula
frase = 'eu sou mais eu'
print(frase.count('e'))
print(frase.islower())