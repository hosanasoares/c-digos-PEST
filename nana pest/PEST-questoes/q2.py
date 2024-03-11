def mensagem_personalizada(nome : str):

    print(f'olá {nome}! Como você está?')



while True:
    nome = str(input('digite um nome:'))
    while nome =='':
        nome = str(input('digite um nome:'))
    if nome == 'sair':
        break
    mensagem_personalizada(nome)