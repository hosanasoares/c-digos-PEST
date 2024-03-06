def comprimentar(nome : str, saudacao : str = 'olá'):
    print(nome, saudacao)
   

nome = str(input('digite um nome: '))
saud = str(input('digite uma saudação:'))



if saud == "":
        comprimentar(saud)
else:
    comprimentar(nome, saud)

comprimentar(nome, saud)
comprimentar('hosana','sua linda')
comprimentar('nana', 'maravilhosa')
comprimentar('maravilhosana','cheirosa')
comprimentar('cheirosana', 'perfeita')
comprimentar('perfeitosana')  # ele vai imprimir o "ola", pois nao esta recebendo o vazio