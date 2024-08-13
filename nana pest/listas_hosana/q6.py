print('lista de compras. Digite o que deseja fazer: [1] adicionar \n[2] Remover \n[3]Ver \n[4]Sair')

lista = []

while True:
    op = str(input('o que deseja fazer: '))

    if op == '1':
        ad = str(input('digite o produto: ')).lower(


        )

        if ad in lista:
            print('já está na lista. ')

        else:
            lista.append(ad)
            print('valor adicionado')

    elif op == '2':
        tirar = str(input('digite o item que deseja tirar: '))

        if tirar in lista:
            lista.remove(tirar)
            print('item removido. ')
        elif lista == []:
            print('Lista está vazia, sem produto para remover. ')

        else:
            print('esse produto não está na lista.')

    elif op == '3':
        print(lista)

    elif op == '4':
        break
    else:
        print('Erro! tente novamente')
print(lista)