def saud(nome : str = 'anonimo', idade: int = 0):
    print(f'olá {nome}, você tem {idade} anos')


pessoa = str(input("digite seu nome: "))
idade = int(input('digite sua idade: '))
saud(idade, pessoa)

saud(idade = idade, nome = pessoa) # precisa tert obrigatoriamente 2 parametros, se esta no def
saud('maria',45)