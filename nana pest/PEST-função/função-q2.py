def cad(nome : str, nome1 : str, idade : int, idade1 : int):
    if idade > idade1:
        print('o mais velho é', nome,'que tem', idade)
    elif idade < idade1:
        print('o mais velho é', nome1,'que tem', idade1)
    else:
        print('o', nome,'e o', nome1,'tem a mesma idade')


nome = str(input('escreva o  nome:'))
idade = int(input('escreva a idade:'))
nome1 = str(input('escreva o segundo nome:'))
idade1 = int(input('escreva a idade:'))

cad(nome, nome1, idade, idade1)